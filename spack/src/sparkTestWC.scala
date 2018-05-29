import org.apache.spark.{SparkConf, SparkContext}

/**
  * Created by zhangheng on 2017/9/6.
  *
  * 练习 用spark 练习  单词书统计
  */
object sparkTestWC {
  def main(args: Array[String]): Unit = {
    //创建一个Spark Context
    val conf = new SparkConf().setAppName("wordCount").setMaster("local")
    val sc = new SparkContext(conf)
    //读取我们的输入数据
    val input = sc.textFile("E:/数据资料/spark/test.txt")
    //把它切成一个个的单词
    val words = input.flatMap(line =>line.split(" "))
    println(words.first())
    //转换为键值对，并计数
    /*
    reduceByKey（）方法的作用，reduceByKey的作用域是key-value类型的键值对，并且是只对每个key的value进行处理，
    如果含有多个key的话，那么久对个values进行处理，这里的函数式我们自己传入的
    x.reduceByKey((pre, after) => (pre + after))
    这里的两个参数 我们逻辑上让他分布代表同一个key 的两个values
    这样，如果输入words = Array(("a", 1), ("b", 1), ("a", 1))
    那么 结果就是 Array（（a,2）,（b,1））

     */
    val counts = words.map(word =>(word,1)).reduceByKey((x,y) => x+y)
//
    println(counts.collect().toBuffer)
    println("lllllllllllllll")
    println(counts.first())
    //将统计出来的单词总数，存入一个文本文件，引发求值
    counts.saveAsTextFile("E:/数据资料/spark/testCount.txt")





  }

}
