package sparkTest
import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.linalg.Vectors
/**
  * Created by zhangheng on 2017/10/31.
  * 练习 spark机器学习  第五章  spark构建分类模型
  *本章主要讨论 spark中常见的三种分类模型，线性模型，决策树模型，朴素贝叶斯模型
  */
object sparkTestWuZhang {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("Simple Application").setMaster("local[*]")
    val sc = new SparkContext(conf)
    val path = "D://实验数据集//fenlei//train.tsv"
      //读取数据
    val rawData  = sc.textFile(path)
    val records = rawData.map(line => line.split("\t"))
    records.take(5).foreach(println)
    //开始的四列 分别包含 url  页面id 原始文本内容  分配给页面 的类别   最后一列为目标值，1 为长久 0 为短暂
   println(records.first().mkString("    "))

    //数据清理  去掉“ 处理 ？ 代替的缺失值
    val data = records.map{
      r => val trimmed = r.map(_.replaceAll("\"",""))
        val label = trimmed(r.size-1).toInt
        //取第5列 到25列 的数据，空缺值用0代替，并转为double 类型
        val features = trimmed.slice(4,r.size-1).map(d => if (d =="?") 0.0 else d.toDouble )
        LabeledPoint(label,Vectors.dense(features))

    }
    //对数据进行缓存，并统计数目
    data.cache()
    println("处理后的数据")
    println(data.first())
    val numData = data.count()
    println("训练样本个数：",numData)
    //朴素贝叶斯要求特征非负 所以数据集要进一步处理
    val nbData = records.map{
      r =>  val trimmed = r.map(_.replaceAll("\"",""))
        val label = trimmed(r.size-1).toInt
        val features = trimmed.slice(4,r.size-1).map(d => if (d =="?") 0.0 else d.toDouble ).map(d =>if (d<0) 0.0 else  d)
        LabeledPoint(label,Vectors.dense(features))
    }

    //训练模型
    import  org.apache.spark.mllib.classification.LogisticRegressionWithSGD
    import  org.apache.spark.mllib.classification.SVMWithSGD
    import  org.apache.spark.mllib.classification.NaiveBayes
    import  org.apache.spark.mllib.tree.DecisionTree
    import  org.apache.spark.mllib.tree.configuration.Algo
    import  org.apache.spark.mllib.tree.impurity.Entropy

    val numIterations = 10 //迭代次数
    val maxTreeDepth = 5// 决策树 最大深度
    //现在依次训练模型，先训练逻辑回归模型
    val lrModel = LogisticRegressionWithSGD.train(data,numIterations)

    //训练SVM模型
    val svmModel = SVMWithSGD.train(data,numIterations)
    //训练贝叶斯模型 记得要处理没有负数的特征值数据
    val nbModel = NaiveBayes.train(nbData)

    //最好训练决策树  注意我们设置模式 或者Algo时，使用了 entroy 不纯度估计
    val dtModel = DecisionTree.train(data,Algo.Classification,Entropy,maxTreeDepth)

    //*************************接下来 看看如何使用这些模型 进行预测*****************
    val dataPoint = data.first
    //用逻辑回归来预测第一条数据
    val prediction = lrModel.predict(dataPoint.features)

    //val prediction1 = lrModel
    //看看实际标签
    val trueLabel = dataPoint.label
    //我们可以将RDD【vector】 整体作为输入预测
    val predictions = lrModel.predict(data.map(lp => lp.features))
    println(predictions.take(5))

    //******************评估模型性能*********************
    //预测的正确率  和错误率
    val lrTotalCorrect = data.map{point => if(lrModel.predict(point.features)== point.label) 1 else  0 }.sum
    val lrAccuracy = lrTotalCorrect/data.count()

    val svmTotalCorrect = data.map{point => if(svmModel.predict(point.features)== point.label) 1 else  0 }.sum
    val nbTotalCorrect = nbData.map{point => if(nbModel.predict(point.features)== point.label) 1 else  0 }.sum

    //注意，决策树的预测阈值 需要明确给出
    val dtTotalCorrect = data.map{
      point => val score = dtModel.predict(point.features)
        val predicted = if(score >0.5) 1 else 0
        if (predicted == point.label) 1 else  0
    }.sum

    //看看其他三个模型的正确率
    val svmAccuracy = svmTotalCorrect/numData
    val nbAccuracy = nbTotalCorrect/numData
    val dtAccuracy = dtTotalCorrect/numData
    println("lrAccuracy",lrAccuracy)
    println("svmAccuracy",svmAccuracy)
    println("nbAccuracy",nbAccuracy)
    println("dtAccuracy",dtAccuracy)

    //准确率 和 召回率
    /*
    在信息检索中 准确率通常用于评价结果的质量，而召回率用来评价结果的完整性
    在二分类问题上 准确率 定义为真阳性的数目除以 假阳性的数目和真阳性数目的和
    真阳性：被正确预测的类别为1 的样本，假阳性是错误预测为类别1的样本

    召回率 = 真阳性除以 真阳性 和假阴性的和。
    假阴性：类别为1 却被预测为0

     */
    //mlib 内置了一系列 方法来计算二分类的pr 和 roc 曲线下的面积  下面我们针对每一个模型 来计算这些指标
    import  org.apache.spark.mllib.evaluation.BinaryClassificationMetrics
    val metrics = Seq(lrModel,svmModel).map{
      model =>val scoreAndLables = data.map{point => (model.predict(point.features),point.label)}
        val metrics = new BinaryClassificationMetrics(scoreAndLables)
        (model.getClass.getSimpleName,metrics.areaUnderPR,metrics.areaUnderROC)


    }
    //朴素贝叶斯，用了nbData数据集，
    val nbmetrics = Seq(nbModel).map{
      model =>val scoreAndLables = nbData.map{point => (model.predict(point.features),point.label)}
        val metrics = new BinaryClassificationMetrics(scoreAndLables)
        (model.getClass.getSimpleName,metrics.areaUnderPR,metrics.areaUnderROC)


    }
    //决策树  ，需要自己指定阈值
    val dtmetrics = Seq(dtModel).map{
      model =>val scoreAndLables = data.map{point => val score = model.predict(point.features)
                                                       (if(score >0.5) 1.0 else 0.0,point.label)
                                             }
        val metrics = new BinaryClassificationMetrics(scoreAndLables)
        (model.getClass.getSimpleName,metrics.areaUnderPR,metrics.areaUnderROC)


    }

    val allMetrics = metrics ++ nbmetrics ++ dtmetrics
    //输出每个模型的 值
    allMetrics.foreach{case (m,pr,roc) => println(f"$m,Area under PR: ${pr*100.00}%2.4f%%,Area under ROC:${roc*100.00}%2.4f%%")}

//************改进模型的性能及参数调优***************************
    import org.apache.spark.mllib.linalg.distributed.RowMatrix
    //RowMatrix 类中有一些操作矩阵的方法，它是一个由向量组成的RDD
    val vectors = data.map(lp =>lp.features)
    val matrix = new RowMatrix(vectors)
    //其中一些方法 可以方便的计算矩阵每列的统计特性
    val matrixSummary = matrix.computeColumnSummaryStatistics()
    //每列的均值
    println(matrixSummary.mean)
    //每列的最小值
    println(matrixSummary.min)
    //每列的最大值
    println(matrixSummary.max)
    //每列的方差
    println(matrixSummary.variance)
    //每列的非0 项的数目
    println(matrixSummary.numNonzeros)

    //**************特征标准化************* 减去均值 除以标准差
    import org.apache.spark.mllib.feature.StandardScaler
    val scaler = new StandardScaler(withMean = true,withStd = true).fit(vectors)
      //标准化 特征
    val scaledData = data.map(lp => LabeledPoint(lp.label,scaler.transform(lp.features)))
    println(data.first.features)
    println(scaledData.first.features)
    //用标准化的数据 重新训练模型

    val lrModelScaled = LogisticRegressionWithSGD.train(scaledData,numIterations)
    //预测的正确率  和错误率
    val lrTotalCorrectScaled = scaledData.map{point => if(lrModelScaled.predict(point.features)== point.label) 1 else  0 }.sum
    val lrAccuracyScaled = lrTotalCorrectScaled/numData
    val lrPredictionsVsTrue = scaledData.map{
      point => (lrModelScaled.predict(point.features),point.label)

    }
    val lrMetricsScaled = new BinaryClassificationMetrics(lrPredictionsVsTrue)
    val ltpr = lrMetricsScaled.areaUnderPR()
    val lrroc = lrMetricsScaled.areaUnderROC()
    println(f"${lrModelScaled.getClass.getSimpleName}\nAccuracy: ${lrAccuracyScaled*100.00}%2.4f%%\nArea under pr:${ltpr*100.00}%2.4f%%\nArea under poc:${lrroc*100.00}%2.4f%%")

//****************其他特征*****************
    //之前我们忽略了 类别category 变量 现在加上
    //首先，我们查看所有类别，并未每个类别做一个索引 1 of k   zipWithIndex.toMap
    val categories = records.map(r => r(3)).distinct.collect.zipWithIndex.toMap
    val numCategories = categories.size
    println("看看 类别 编码")
    println(categories)
    println(numCategories)
    //因此，我们需要穿件一个长为14 的向量来表示列表特征，然后根据每个样本所属类别索引，对相应的维度赋值为1 ，其他值为0
    //我们假设这个新的特征向量和其他的数值向量一样
    val dataCategories = records.map{
      r => val trimmed = r.map(_.replaceAll("\"",""))
        val lable = trimmed(r.size-1).toInt
        val categoryIdx = categories(r(3))
        val categoryFeatures = Array.ofDim[Double](numCategories)
        categoryFeatures(categoryIdx) = 1.0
        val otherFeatures = trimmed.slice(4,r.size-1).map(d =>if(d == "?") 0.0 else d.toDouble)
        val features = categoryFeatures ++ otherFeatures
        LabeledPoint(lable,Vectors.dense(features))
    }
    println("增加向量特征后的  特征集合")
    println(dataCategories.first)
    println(dataCategories.first.features.size)
//标准化
    val scalerCats = new StandardScaler(withMean = true, withStd = true).
      fit(dataCategories.map(lp => lp.features))
    val scaledDataCats = dataCategories.map(lp =>
      LabeledPoint(lp.label, scalerCats.transform(lp.features)))

//可以使用如下代码看到标准化之前的特征：
    println(dataCategories.first.features)
    //可以使用如下代码看到标准化之后的特征：
    println(scaledDataCats.first.features)
    //训练，并查看结果
    val lrModelScaledCats = LogisticRegressionWithSGD.train(scaledDataCats,
      numIterations)
    val lrTotalCorrectScaledCats = scaledDataCats.map { point =>
      if (lrModelScaledCats.predict(point.features) == point.label) 1 else 0
    }.sum
    val lrAccuracyScaledCats = lrTotalCorrectScaledCats / numData
    val lrPredictionsVsTrueCats = scaledDataCats.map { point =>
      (lrModelScaledCats.predict(point.features), point.label)
    }
    val lrMetricsScaledCats = new BinaryClassificationMetrics(lrPredictionsVsTrueCats)
    val lrPrCats = lrMetricsScaledCats.areaUnderPR
    val lrRocCats = lrMetricsScaledCats.areaUnderROC
    println(f"${lrModelScaledCats.getClass.getSimpleName}\nAccuracy: ${lrAccuracyScaledCats * 100}%2.4f%%\nArea under PR: ${lrPrCats * 100.0}%2.4f%%\nArea under ROC: ${lrRocCats * 100.0}%2.4f%%")

println("*******************************参数调优****************************")
    //逻辑回归和 SVM 模型有相同的参数，原因是它们都使用随机梯度下降（ SGD ）作为基础优化技术







  }

}
