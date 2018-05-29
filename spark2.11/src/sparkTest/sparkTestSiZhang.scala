package sparkTest

import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.mllib.recommendation.ALS
import org.apache.spark.mllib.recommendation.Rating
import org.apache.spark.mllib.evaluation.{RankingMetrics, RegressionMetrics}
import org.jblas
/**
  * Created by zhangheng on 2017/10/30.
  */
object sparkTestSiZhang {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("Simple Application").setMaster("local[*]")
    val sc = new SparkContext(conf)
    var path = "D://实验数据集//ml-100k//u.data"
    val rawDtata = sc.textFile(path)
    println(rawDtata.first())
    //从数据中提取用户id  影片 id  和评价星级
    val rawRating = rawDtata.map(line =>line.split("\t")).map(pur =>(pur(0),pur(1),pur(2)))
    //val rawRating = rawDtata.map(_.split("\t").take(3))  //简单的写法
    println(rawRating.first())

    //对数据进行处理，从而创建所需要的评级数据集  把之前的从文本中读出的数据  转成Rating类型的数据 ，这是spark 的mlib要求的
    val ratings = rawRating.map{case  (user,movie,rating)  => Rating(user.toInt,movie.toInt,rating.toDouble)}

    println(ratings.first())
    println(ratings.count())
    //下面使用 spark MLIB 来训练模型

    //矩阵分解模型  svd ，spark采用的交替最小二乘法 来解 ，
    /*
    参数 解释  ALS.train (ratings,rank,iterations,lambda )：
    rank: 对应 ALS模型中因子个数 也就是低阶 近似矩阵中 隐含特征个数
    iterations: 迭代次数  10 次左右
    lambda：改参数 控制模型的正则化过程

     */
    val rank = 50
    val iterations = 20
    val lambda = 0.01
    //ratings 是数据集
    val model = ALS.train(ratings,rank,iterations,lambda)

    println(model.userFeatures)
    println(model.userFeatures.count())
    println(model.productFeatures.count())

    println(model.userFeatures.first())
    println(model.productFeatures.first())

    //*******************************************用户推荐***************
    //训练完模型，用该模型进行预测
    //预测给定用户对给定物品的预期得分
    val predictedRating = model.predict(789,123)
    println(predictedRating)
    //predict 函数同样可以传入一组数据，，这时它将为每一对都生成相应的预测得分
    //要为某一个用户  生成前k 个推荐的商品，可以利用一下 函数，传入 用户id 和 要推荐的物品的个数
    //给用户推荐10个商品，主要利用点积方法，算出得分最高的前十个商品  给用户推荐
    val topKPecs = model.recommendProducts(789,10)
    println(topKPecs.mkString("\n"))

//***************物品推荐**************
    //物品推荐：给定一个物品，有哪些物品 与它相似，这里的相似，取决于 具体的定义 。大多数情况下，相似度是通过某种
    //方式比较两个物品的向量而 得到的。
    //常见的相似度 包括： 皮尔森相关系数，余弦相似度， 杰卡德相似系数

    //现在我们 先用余弦相似度 来计算
    import  org.jblas.DoubleMatrix
    val aMatrix = new DoubleMatrix(Array(1.0,2.0,3.0))
    println("aMatrix",aMatrix)
//余弦 相似度 计算公式
    def cosineSimilarity(v1:DoubleMatrix,v2:DoubleMatrix): Double ={
      v1.dot(v2)/(v1.norm2()*v2.norm2())
    }

    //获取某物品 对应的向量因子
    val itemID = 567
    val itemFactor = model.productFeatures.lookup(itemID).head
    //转换数据类型
    val itemVector = new DoubleMatrix(itemFactor)
    //计算与自身的相似度
    val cos = cosineSimilarity(itemVector,itemVector)

    //现在求 各个物品的余弦相似度
    val sims = model.productFeatures.map{ case (id ,factor)  =>
        val factorVector = new  DoubleMatrix(factor)
        val sim = cosineSimilarity(factorVector,itemVector)
        (id,sim)

    }
    //对物品相似度 进行排序，然后计算最相似 前 10 的商品
    var K = 10
    val sordSims = sims.top(K)(Ordering.by[(Int,Double),Double]{case (id,similarity) => similarity})
    //最后 打印这10 个给定物品最相似的物品
    println(sordSims.take(10).mkString("\n"))

    val sordSims2 = sims.top(K+1)(Ordering.by[(Int,Double),Double]{case (id,similarity) => similarity})

    var movies = sc.textFile(    "D://实验数据集//ml-100k//u.item")
    //电影id 到标题的影射
    val titles = movies.map(line => line.split(",").take(2)).map(array  => (array(0).toInt,array(1))  ).collectAsMap()

    val tt = sordSims2.slice(1,11).map{ case (id,sim)  => (titles(id),sim) }.mkString("\n")
    println(tt)

    //模型评估

    //均方差  （mean squared error ，MSE） 定义为：平方误差 除以 总数目 （平方误差= 预测到评级与真实评级的差值的平方）
   val usersProducts = ratings.map{ case Rating(user,product,rating) =>(user,product)}
    val predictions = model.predict(usersProducts).map{case Rating(user,product,rating) =>((user,product),rating)  }


    val ratingsAndPredictions = ratings.map{
      case Rating(user,product,rating) => ((user,product),rating)
    }.join(predictions)

    val predictedAndTrue = ratingsAndPredictions.map{case ((user,product),(preducted,actual)) => (preducted,actual)}
    val regressionMetrics = new RegressionMetrics(predictedAndTrue)
    println(" MSE",regressionMetrics.meanSquaredError)
    println(" RMSE",regressionMetrics.rootMeanSquaredError)

    //MAP  这一部分  暂时没有完成
    /*
    val allRecs = model.userFeatures.map{case (userID,array) =>
    val userVector = new DoubleMatrix(array)
        val scores = imBroadcast.value.mmul(userVector)

    }

    val predictedAndTrueForRanking = allRect.join(userMovices)
    */




















  }

}
