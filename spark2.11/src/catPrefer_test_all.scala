/**
  * Created by zhangheng on 2017/10/19.
  */

import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf
import org.apache.spark.broadcast.Broadcast
import org.apache.spark.ml.feature.{OneHotEncoder, StringIndexer}
import org.apache.spark.ml.feature.{IndexToString, StringIndexer}
import org.apache.spark.mllib
import org.apache.spark.mllib.linalg.{Vector, Vectors}
import org.apache.spark.sql.hive.HiveContext
import org.apache.spark.sql.Row
import org.apache.spark.sql.types.{StructType,StructField,StringType}
import org.apache.spark.mllib.linalg.{Matrices, Matrix}
import org.apache.spark.mllib.linalg.distributed.RowMatrix
import org.apache.spark.mllib.linalg.distributed.IndexedRowMatrix
import org.apache.spark.mllib.linalg.SingularValueDecomposition
import org.apache.spark.rdd.RDD
import org.apache.spark.mllib.linalg.distributed.{CoordinateMatrix, MatrixEntry}
import org.apache.spark.mllib.linalg.{DenseMatrix}
import org.apache.spark.mllib.recommendation.ALS
import org.apache.spark.mllib.recommendation.MatrixFactorizationModel
import org.apache.spark.mllib.recommendation.Rating

import scala.collection.mutable
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Calendar
import java.lang.String
import scala.collection.immutable.ListMap

object catPrefer_test_all {
  def main(args: Array[String]) {
    //val conf = new SparkConf().setAppName("Simple Application")
    val conf = new SparkConf().setAppName("Simple Application").setMaster("local[*]")
    val sc = new SparkContext(conf)
    val hiveContext = new HiveContext(sc)
    sc.setLogLevel("WARN")

    //获取当前时间
    var dateFormat: SimpleDateFormat = new SimpleDateFormat("yyyy-MM-dd")
    var cal: Calendar = Calendar.getInstance()
    cal.add(Calendar.DATE, -1)
    var yesterday = dateFormat.format(cal.getTime())

    //获得用户对已购买商品的得分
    //val userCat = hiveContext.sql("select id, cat, score from temp.cat_count_sort where dt = '2017-09-13' limit 5000" )
    val userCat = hiveContext.sql("select id, cat, score from temp.cat_count_sort where dt = '2017-09-26' ")
    println("显示读出的数据")
    //println(userCat.show(100))
    val ratings = userCat.map(row => Rating(row.getInt(0), row.getInt(1), row.getDouble(2)))

    println("读取100句")
    println("ratings " + ratings.count())
    //println(ratings)
    println("获得用户对已购买商品的得分")



    // Build the recommendation model using ALS
    val rank = 40
    val numIterations = 20
    //val alpha = 0.0001
    val lambda = 0.02
    //val model = ALS.trainImplicit(ratings, rank, numIterations, lambda, alpha)
    val model = ALS.train(ratings, rank, numIterations, lambda)
    //val broadcastModel = sc.broadcast(model)
    println("获得协同过滤模型")
    println("测试 得分  OOOOOOOOOOOOOOOO")
    println(model.predict(9, 12))

    //一. 生成物品相似度矩阵
    val productFeature = model.productFeatures.collect()
    println("看看productFeature")
    println(productFeature)
    val itemSim = new mutable.HashMap[(Int, Int), Double]()
    val ite1 = productFeature.iterator
    while (ite1.hasNext) {
      val product = ite1.next()
      val ite2 = productFeature.iterator
      while (ite2.hasNext) {
        val iteTmp = ite2.next()
        if(product._1==17) {
          itemSim.put((product._1, iteTmp._1), getSimilarity(product._2, iteTmp._2))
        }
      }
    }
    var k = 0
    println("输出相似矩阵")
    println( ListMap(itemSim.toSeq.sortBy(_._2):_*))
  //  println("*********")
   // for( i <- itemSim ) println(i)






    /*

    //获得品类向量
    val catVec = ratings.map{ case Rating(user, product, rate) =>
      (product, user)
    }.groupByKey().map{ productArray =>
      val product = productArray._1
      val userArray = productArray._2.toArray.sortBy(x=>x)
      (product, userArray)
    }

    //获得所有用户
    hiveContext.sql("drop table temp.all_uid_cat")
    hiveContext.sql("create table temp.all_uid_cat (id int)")
    //hiveContext.sql("insert into table temp.all_uid partition(dt='2017-0-8-21') select distinct id from temp.cat_brand_count_sort limit " + args(0))
    hiveContext.sql("insert into table temp.all_uid_cat select distinct id from temp.have_phone_cat_count_sort where dt = '2017-09-28' sort by id ")
    //hiveContext.sql("insert into table temp.all_uid_brand select distinct id from (select id, brand, score from temp.brand_count_sort where dt = '2017-09-13' limit 5000)a")
    val users = hiveContext.sql("select id from temp.all_uid_cat").collect()
    var usersCount:Int = users.length
    var uesrsLocal: Array[Int] = new Array[Int](usersCount)
    for (i <- 0 until usersCount) {
      uesrsLocal(i) = users.apply(i).getInt(0)
    }
    println("获得所有用户 " +  usersCount)

    //一. 生成物品相似度矩阵
    val ite1 = productFeature.iterator
    while(ite1.hasNext){
      val product = ite1.next()
      val ite2 = productFeature.iterator
      while (ite2.hasNext) {
        val iteTmp  = ite2.next()
        itemSim.put((product._1, iteTmp._1), getSimilarity(product._2, iteTmp._2))
        println("product1 " + product._1 )
        println(product._2.mkString(","))
        println("product2 " + iteTmp._1 )
        println(iteTmp._2.mkString(","))
        println(product._1, iteTmp._1, getSimilarity(product._2, iteTmp._2))
      }
    }
    var itemSimBroadcast = sc.broadcast(itemSim)

  }*/
  }

  //计算向量相似度
  def getSimilarity(productA: Array[Double], productB: Array[Double]): Double = {
    var result = 0.0

    val numerator = productA.zip(productB).map(d => d._1 * d._2).reduce(_ + _).toDouble
    val denominator_1 = math.sqrt(productA.map(num => {
      math.pow(num, 2)
    }).reduce(_ + _))
    val denominator_2 = math.sqrt(productB.map(num => {
      math.pow(num, 2)
    }).reduce(_ + _))
    if (denominator_1 != 0 & denominator_2 != 0) {
      result = numerator / (denominator_1 * denominator_2)
    }
    else {
      result = 0
    }
    result
  }
}





