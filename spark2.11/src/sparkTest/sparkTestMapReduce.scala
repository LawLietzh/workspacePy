package sparkTest

import org.apache.spark.{SparkConf, SparkContext}

/**
  * Created by zhangheng on 2017/10/30.
  * 练习 map 和reduce ，
  * http://blog.csdn.net/jewes/article/details/39896301
  */
object sparkTestMapReduce {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("Simple Application").setMaster("local[*]")
    val sc = new SparkContext(conf)
    //map map是对RDD 的每个元素都执行一个指定的函数来参数
    val a = sc.parallelize(1 to 9,3)
    val b = a.map(x => x*2)
    //把结果 打印出来 ,收集 ，选择个数，打印
    b.collect().take(5).foreach(println)


    //reduce 将RDD中元素两两传递给输入函数，同时产生一个新的值，新产生的值 与RDD中下一个元素在被传递给输入函数直到最后只有一个值为止
    val c = sc.parallelize(1 to 10)
    var d = c.reduce((x,y) => x+y)
   println(d)

   // reduceByKey  就是对元素为 kv对的RDD中key相同的元素的value 进行reduce ，因此key相同的多个元素值被reduce为一个值
    val e = sc.parallelize(List((1,2),(3,4),(3,6)))
    val f = e.reduceByKey((x,y) => x+y).collect
    f.foreach(println)
    // 实验
    var aa = 0
    var bb = 5

    try{
      bb/aa
      println("我是try")
    } catch{
      case e:ArithmeticException => println(e)
    }



  }

}
