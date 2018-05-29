package sparkTest

import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.{SparkConf, SparkContext}

/**
  * Created by zhangheng on 2017/10/31.
  *  练习 spark机器学习  第六章  spark构建回归模型
  *  h回归模型的预测目标是实数变量，分类模型的预测目标是类别编号
  *
  */
object sparkTestLiuZhang {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("Simple Application").setMaster("local[*]")
    val sc = new SparkContext(conf)
    val path = "D://实验数据集//fenlei//train.tsv"
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

    lrModel.clearThreshold()
    val dataPoint = data.first()
    //用逻辑回归来预测第一条数据
    val prediction = lrModel.predict(dataPoint.features)
    lrModel.clearThreshold()
    println(prediction)

    val predictions = lrModel.predict(data.map(lp => lp.features))
    println(predictions.take(5).mkString("     "))

    lrModel.clearThreshold()

  }

}
