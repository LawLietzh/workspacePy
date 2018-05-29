
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
/**
  * Created by zhangheng on 2017/10/18.
  */
object catPrefer_test_model {
  def main(args: Array[String]) {
    println("dddddddddddddddddddd")
    //val conf = new SparkConf().setAppName("Simple Application")
    val conf = new SparkConf().setAppName("Simple Application").setMaster("local[*]")
    val sc = new SparkContext(conf)
    val hiveContext = new HiveContext(sc)
    sc.setLogLevel("WARN")

    //获取当前时间
    var dateFormat:SimpleDateFormat = new SimpleDateFormat("yyyy-MM-dd")
    var cal:Calendar=Calendar.getInstance()
    cal.add(Calendar.DATE,-1)
    var yesterday=dateFormat.format(cal.getTime())

    //获得用户对已购买商品的得分
    println("yesterday " + yesterday)
    //val userCat = hiveContext.sql("select id, cat, score from temp.cat_count_sort where dt = '2017-09-13' limit 5000" )
    val userCat = hiveContext.sql("select id, cat, score from temp.cat_count_sort where dt = '2017-09-26' limit 2000000")
    val ratings = userCat.map( row => Rating(row.getInt(0), row.getInt(1), row.getDouble(2)))
    val ratingsLocal = ratings.collect()
    println("ratings " + ratings.count())
    println("获得用户对已购买商品的得分")

    // Build the recommendation model using ALS
    val rank = 61
    val numIterations = 10
    //val alpha = 0.0001
    val lambda = 0.01
    //val model = ALS.trainImplicit(ratings, rank, numIterations, lambda, alpha)
    val model = ALS.train(ratings, rank, numIterations, lambda)
    //val broadcastModel = sc.broadcast(model)
    println("获得协同过滤模型")

    val usersProducts = ratings.map { case Rating(user, product, rate) =>
      (user, product)
    }
    //val usersProductsLocal = usersProducts.collect()

    val predictions =
      model.predict(usersProducts).map { case Rating(user, product, rate) =>
        ((user, product), rate)
      }.sortByKey()
    val predictionsLocal = predictions.collect()

    val ratesAndPreds = ratings.map { case Rating(user, product, rate) =>
      ((user, product), rate)
    }.join(predictions)
    //val ratesAndPredsLocal = ratesAndPreds.collect()

    val MSE = ratesAndPreds.map { case ((user, product), (r1, r2)) =>
      println(user + " " + product + " real: " + r1 + " predict: " + r2)
      val err = (r1 - r2)
      err * err
    }.mean()
    println("mse " + MSE)
    /*
    //一. 生成物品相似度矩阵
    val productFeature = model.productFeatures.collect()
    val itemSim = new mutable.HashMap[(Int,Int), Double]()
    val ite1 = productFeature.iterator
    while(ite1.hasNext){
      val product = ite1.next()
      val ite2 = productFeature.iterator
      while (ite2.hasNext) {
        val iteTmp  = ite2.next()
        itemSim.put((product._1, iteTmp._1), getSimilarity(product._2, iteTmp._2))
        println(product._1, iteTmp._1, getSimilarity(product._2, iteTmp._2))
      }
    }
    var itemSimBroadcast = sc.broadcast(itemSim)
    */

    /*
        //获得各品类的复购率
        val secondBuy = hiveContext.sql("select cast(cat as int), probability from dm_tag.cat_buy_twice where dt='"  + yesterday + "'").collect()
        val secondBuyRate = new mutable.HashMap[Int, Double]()
        for(i <- 0 until secondBuy.length)
          secondBuyRate.put(secondBuy.apply(i).getInt(0),secondBuy.apply(i).getDouble(1))

        val broadcastSecondBuy: Broadcast[mutable.HashMap[Int,Double]] = sc.broadcast[mutable.HashMap[Int,Double]](secondBuyRate)
        println("获得品类的复购率 " + "品类个数 " + secondBuy.length)

        //二. 生成物品评分
        //获得所有用户
        hiveContext.sql("drop table temp.all_uid_cat")
        hiveContext.sql("create table temp.all_uid_cat (id int)")
        //hiveContext.sql("insert into table temp.all_uid partition(dt='2017-0-8-21') select distinct id from temp.cat_brand_count_sort limit " + args(0))
        hiveContext.sql("insert into table temp.all_uid_cat select distinct id from temp.have_phone_cat_count_sort where dt = '"  + yesterday + "' sort by id ")
        //hiveContext.sql("insert into table temp.all_uid_brand select distinct id from (select id, brand, score from temp.brand_count_sort where dt = '2017-09-13' limit 5000)a")
        val users = hiveContext.sql("select id from temp.all_uid_cat ")
        val usersLength = users.count()
        println("获得所有用户 " + usersLength.toString)

        //获得所有cat
        hiveContext.sql("drop table temp.all_cat")
        hiveContext.sql("create table temp.all_cat (cat int)")
        hiveContext.sql("insert into table temp.all_cat select distinct cat from temp.have_phone_cat_count_sort where dt = '" + yesterday + "'")
        //hiveContext.sql("insert into table temp.all_brand select distinct brand from (select id, brand, score from temp.brand_count_sort where dt = '2017-09-13' limit 5000)a")
        val cat = hiveContext.sql("select cat from temp.all_cat").collect()
        var catCount:Int = cat.length
        var catLocal: Array[Int] = new Array[Int](catCount)
        for (i <- 0 until catCount) {
          catLocal(i) = cat.apply(i).getInt(0)
        }
        println("获得所有cat " + "cat " + catCount )
        val broadcastCat: Broadcast[Array[Int]] = sc.broadcast[Array[Int]](catLocal)

        /*
        //生成用户对所有商品的对应
        var userAllProducts = users.map { user =>
          var userProduct = new Array[(Int, Int)](broadcastCat.value.length)
          var ite = broadcastCat.value.iterator
          var num = 0
          while(ite.hasNext) {
            userProduct(num) = (user.getInt(0), ite.next())
            num += 1
          }
          userProduct
        }.flatMap(a=>a)
        //.repartition(,10)
        println("所有用户对所有商品的对应")
        //val userAllProductsLocal = userAllProducts.collect()*/

        // 得到用户已购买的商品
        val userBuyProducts = ratingsValid.map { case Rating(user, product, rate) =>
          (user, (product, rate))
        }.groupByKey().map{case (user, buyProduct) =>
          var buy = new mutable.HashMap[Int, Double]
          val ite = buyProduct.iterator
          while(ite.hasNext){
            var tmp = ite.next()
            buy.put(tmp._1, tmp._2)
          }
          (user, buy)
        }
        println("得到用户已购买的商品")
        println("userBuyProducts:"+userBuyProducts.count())
        //val userBuyProductsLocal = userBuyProducts.collect()

        /*
        //获得用户对所有商品的最终评分矩阵
        val userIsBuyAndScorePrepare = userAllProducts.groupByKey().join(userBuyProducts)
        //var userIsBuyAndScorePrepareLocal = userIsBuyAndScorePrepare.collect()*/

        //获得用户所有已购买物品复购得分和未购买物品得分前10名
        val userCatScore: RDD[(String, String, String, Double)] = userBuyProducts.map { case (user, buyProduct) =>
          var productAndIsBuyAndScoreBuy = new Array[(String, String, String, Double)](buyProduct.size)
          var productAndIsBuyAndScoreNotBuy = new Array[(String, String, String, Double)](broadcastCat.value.length - buyProduct.size)
          //println("notBuy length " + (broadcastBrand.value.length - buyProduct.keySet.size))
          val ite = broadcastCat.value.iterator
          var buyNum = 0
          var notBuyNum = 0
          while(ite.hasNext) {
            var isBuy = 0
            val product = ite.next()
            if (buyProduct.contains(product)){
              isBuy = 1
            }
            var score:Double = 0.0
            if(isBuy == 0) {
              var keyIte = buyProduct.keySet.iterator
              while(keyIte.hasNext){
                var key = keyIte.next()
                var scoreTmp = buyProduct.get(key).get * itemSimBroadcast.value.get(key, product).get
                if(scoreTmp == null)
                  scoreTmp = 0
                score += scoreTmp
              }
              productAndIsBuyAndScoreNotBuy(notBuyNum) = (user.toString, product.toString ,isBuy.toString, score)
              notBuyNum = notBuyNum+1
            }
            else{
              if(broadcastSecondBuy.value.contains(product))
                score = broadcastSecondBuy.value.get(product).get.asInstanceOf[Double]
              else
                score = 0
              productAndIsBuyAndScoreBuy(buyNum) = (user.toString, product.toString ,isBuy.toString, score)
              buyNum = buyNum+1
            }
            //println("notBuyNum " + notBuyNum)
          }
          var productAndIsBuyAndScoreFinal = new Array[(String, String, String,Double)](buyProduct.size + 10)
          var num = 0
          var buyProductScoreIte = productAndIsBuyAndScoreBuy.iterator
          while(buyProductScoreIte.hasNext){
            productAndIsBuyAndScoreFinal(num) = buyProductScoreIte.next()
            num = num+1
          }
          productAndIsBuyAndScoreNotBuy = productAndIsBuyAndScoreNotBuy.sortWith((a,b) => a._4 > b._4)
          var notBuyProductScoreIte = productAndIsBuyAndScoreNotBuy.iterator
          var count = 0
          while(count < 10){
            productAndIsBuyAndScoreFinal(num) = notBuyProductScoreIte.next()
            count = count+1
            num = num+1
          }
          productAndIsBuyAndScoreFinal
        }.flatMap(a=>a)
        println("获得用户对所有商品的最终评分矩阵")
        println("矩阵count:"+userCatScore.count())
        //val userBrandScoreLocal = userBrandScore.collect()

        //三. 将计算结果存入hive
        val schemaString = "hastid id cat is_buy score"
        val schema = StructType(schemaString.split(" ").map(fieldName=>StructField(fieldName, StringType, true)))
        val rowRDD = userCatScore.map(line => Row(line._1+line._2.hashCode.toString, line._1, line._2, line._3, line._4.toString))
        val userCatScoreDataFrame = hiveContext.createDataFrame(rowRDD, schema)
        //hiveContext.sql("use temp")
        userCatScoreDataFrame.registerTempTable("cat_prefer")
        hiveContext.sql("drop table temp.cat_prefer")
        hiveContext.sql("create table temp.cat_prefer(id string, cat string, is_buy string, score string) stored as parquet")
        var result = hiveContext.sql("insert into table temp.cat_prefer select id, cat, is_buy,score from cat_prefer")
        println("结果存入临时表")

        hiveContext.sql("alter table dm_tag.cat_prefer drop if exists partition(dt='" + yesterday + "')")
        hiveContext.sql("insert into table dm_tag.cat_prefer partition(dt = '" + yesterday + "') " +
          "select b.uid, c.cat2_id, a.is_buy, a.score " +
          " from (select * from temp.cat_prefer) a " +
          "join (select * from temp.uid_sort where dt = '" + yesterday + "') b on a.id = b.id " +
          "join (select * from temp.cat_sort where dt = '" + yesterday + "') c on a.cat = c.cat " )
        println("最终结果存入hive")

        var k = 0*/
  }


  //计算向量相似度
  def getSimilarity(productA:Array[Double], productB: Array[Double]): Double={
    val numerator = productA.zip(productB).map(d => d._1*d._2).reduce(_+_).toDouble
    val denominator_1 = math.sqrt(productA.map(num => {math.pow(num,2)}).reduce(_+_))
    val denominator_2 = math.sqrt(productB.map(num => {math.pow(num,2)}).reduce(_+_))
    numerator / (denominator_1*denominator_2)
  }
}



