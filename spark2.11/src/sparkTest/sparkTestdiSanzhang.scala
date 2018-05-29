package sparkTest

import org.apache.spark.{SparkConf, SparkContext}

/**
  * Created by zhangheng on 2017/10/27.
  * 这部分主要练习， spark机器学习第三章，电影推荐
  */
object sparkTestdiSanzhang {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("Simple Application").setMaster("local[*]")
    val sc = new SparkContext(conf)

    val path = "D://实验数据集//ml-100k//u.user" //这个文件是用户信息，主要有的字段：id，age，gender，occupation ,ZIP code
    val user_data = sc.textFile(path)
    println(user_data.first())

    //统计一些信息.
    val user_fields = user_data.map( line =>line.split(","))
    println(user_fields)
    val num_user = user_fields.map(  pur => pur(0)  ).count()
    println("num_user",num_user)
    //性别种类
    val num_genders = user_fields.map(pur => pur(2)).distinct().count()
    println("num_genders",num_genders)
    //用matplotlib 来画直方图  分许用户年龄的分布情况
    val age = user_fields.map( x => x(1).toInt ).collect()
    //计算用户的职业分布情况
    val count_by_occupation = user_fields.map(pur =>(pur(3),1)).reduceByKey(_ + _).collect()
    //遍历输出
    for (i <- 1 to 5){
      println(count_by_occupation(i))
    }

    println("   ********* 开始探索 电影数据     ***********")
    val movie_data = sc.textFile("D://实验数据集//u.item")
    println(movie_data.first())
    val num_movies = movie_data.count()
    println("num_movies",num_movies)
    //抽取电影年龄

    val movie_fields = movie_data.map(line => line.split("|"))
    println(movie_fields.count())
    //val year = movie_fields.map(pur =>(pur(1))).map(x =>convert_year(x))
    //year.foreach(println)
   // val year_filtered = year.filter(x =>x !="1900")
    //统计不同年龄电影的数目
   // val movie_ages = year_filtered.map(yr => 2017- yr.toInt).countByValue()

    println("kkkkkkkkkkkkkkkkkkk看看评级数据")
    val rating_data = sc.textFile("D://实验数据集//ml-100k//u.data")
    println(rating_data.first())
    val num_rating = rating_data.count()
    println("评论条数：",num_rating)
    //取得 评级 的级别
    val rating = rating_data.map(line =>line.split("\t")).map(pur =>pur(2).toInt)
    // 第一次写 匿名函数，
    val maxrating = rating.reduce( (x,y) =>  if(x>y) x else y )
    println("maxrating",maxrating)
    val minrating = rating.reduce( (x,y) =>  if(x>y) y else x )
    println("minrating",minrating)
    // spark 提供了一个 states 的统计函数 用来统计
    // 统计的有 总行数， 均值，标准差，最大值，最小值
    val sta = rating.stats() //这里要求数据是 int 类型之类的 数据类型
    println(sta)
    //来对评级以用户ID为主键进行分组
     val user_ratings_grouped = rating_data.map(put =>(put(0).toInt,1)).reduceByKey(_ + _).collect()
    user_ratings_grouped.take(5).foreach(println)


















  }

}
