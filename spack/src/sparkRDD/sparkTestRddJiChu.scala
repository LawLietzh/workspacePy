package sparkRDD
import org.apache.spark.{SparkConf, SparkContext}
/**
  * Created by zhangheng on 2017/9/6.
  * 主要联系Spark 对数据的核心抽象-- 弹性分布式数据集  RDD
  * RDD 其实 就是分布式的元素集合   ，在Spark中，对数据的所以操作不外乎，创建RDD，转化已有的RDD，以及调用RDD操作进行求值
  * 而在这一切的背后，Spark会自动将RDD中数据分发到集群上，并将操作并行化处理
  */
object sparkTestRddJiChu {
  def main(args: Array[String]): Unit = {
    //初始化
    //创建一个Spark Context
    val conf = new SparkConf().setAppName("wordCount").setMaster("local")
    val sc = new SparkContext(conf)
    //创建RDD 有两种方式，一是读取文件，而是建立对象集合（list 或set）
    //按行读取到一个集合
    val input = sc.textFile("E:/数据资料/spark/test.txt")
    val data = Array(1,2,3,4,5,6,6)
    //集合中的元素被复制到 一个可并行操作 的分布式数据集中，
    val distData = sc.parallelize(data)
    val data1 = Array(1,2,3,4,5)
    //集合中的元素被复制到 一个可并行操作 的分布式数据集中，
    val distData1 = sc.parallelize(data1)
    val shabi = distData1.union(distData)
    println("shshshshshhshshshshhshshhhhhhhhhhhhhhhhh")
    shabi.foreach(println)


    // 创建出来后，RDD支持两种类型的操作：转化操作（transformation） 和  行动操作（action）
    //如何区别 转化操作 和行动操作   你可以看看它的返回值类型：转化操作返回的是 RDD，而行动操作返回的是其他的数据类型。
    /*
    转化操作会有一个RDD 生成一个新的RDD。例如，筛选操作
    转化操作和行动操作的区别 计算RDD的方式不同。在于Spark 只会 惰性的计算这些RDD。它们只有第一次在一个行动操作中用到
    时，才会真正计算。这种策略刚开始看起来可能会显得有些奇怪，不过在大数据领域是很
     有道理的。
     事实上，在行动操作 first() 中，Spark 只需要扫描文件直到找到第一个匹配
    的行为止，而不需要读取整个文件。
    最后，默认情况下，Spark 的 RDD 会在你每次对它们进行行动操作时重新计算。如果想
    在多个行动操作中重用同一个 RDD，可以使用 RDD.persist() 让 Spark 把这个 RDD 缓存
   下来。

(1) 从外部数据创建出输入 RDD。
(2) 使用诸如 filter() 这样的转化操作对 RDD 进行转化，以定义新的 RDD。
(3) 告诉 Spark 对需要被重用的中间结果 RDD 执行 persist() 操作。
(4) 使用行动操作（例如 count() 和 first() 等）来触发一次并行计算，Spark 会对计算进行
优化后再执行。


     */

    /*
    flatMap 和 Map的区别
    总结：1. map会将每一条输入映射为一个新对象。{苹果，梨子}.map(去皮） = {去皮苹果，去皮梨子}     其中：   “去皮”函数的类型为：A => B
          2. flatMap包含两个操作：会将每一个输入对象输入映射为一个新集合，然后把这些新集合连成一个大集合。
             {苹果，梨子}.flatMap(切碎)  = {苹果碎片1，苹果碎片2，梨子碎片1，梨子碎片2}
             其中：   “切碎”函数的类型为： A => List<B>

     */
    val words =  input.flatMap(line =>line.split(" "))
    val wordss = words.persist()//把这个结果缓存起来
    val scalines = words.filter(line => line.contains("wo"))
    //调用first（）行动操作
    val nums = scalines.first()
    println(nums)



      //转化操作  RDD的转化操作是返回新的RDD的操作，转化出来的RDD是惰性求值的，只有在行动操作用用到这些RDD时才会被计算

    val dayinchulai = words.union(scalines)
    println(dayinchulai.first())

    //行动操作  他们会把最终求得的结果返回带驱动器程序 或者写入外部存储系统
    //因此，需要生产实际的输出
    //输出结果 ，三个结果
    /*
      我们在驱动器程序中使用take（）获取Rdd中少量元素，然后在本地遍历这些元素。
      只有当你的整个数据集能在单台机器的内存中放得下时，才能使用 collect() ，因此， collect() 不能用在大规模数据集上。

      你可以使用 saveAsTestFile ,savaAsSequenceFile()等把数据内用一各种自带的格式保存下来
     */
    words.take(5).foreach(println)


    println("************常见的RDD操作****************")
    //针对各个元素的转化操作
    /*
      map() 和 flatMap()
      转化操作map 接收一个函数，把这个函数用于RDD中的每一个元素
      map主要处理，没每一个元素都进行处理，
      flatMap 主要是处理一行数据，传出处理这一行函数的，返回一个列表
     */
    val result = distData.map(x => x*x)
    println("hhhhhhhhhh:  ",result.collect())//(hhhhhhhhhh:  ,[I@6ae62c7e)
    println(result.collect().mkString(","))  //1,4,9,16,25

    val str = sc.parallelize(List("hello word","hai hai hai"))
    val wor = str.flatMap(line =>line.split(" "))
    wor.take(5).foreach(println)

    //RDD不是严格的集合，但是支持许多数学上的集合操作，
    /*
      RDD.distinct() 作用：去除重复数据。转化操作来生成一个包含不同原始的RDD，这个操作开销很大
      一些简单的集合操作，
    （1） union（)  合并两个RDD  ，与数学中的union(）操作不同的是，如果输入的RDD中重复数据，spark的union（）操作来回包含这些重复数据
    （2） intersection()与union类似，但是会去掉 重复的元素，单个RDD的重复元素也会一起移除
    （3） subtract（）函数接收另一个RDD作为参数，返回一个只包含第一个RDD，不包含第二个RDD的元素
    （4） cartesian()做笛卡尔积，返回所有 可能的(a,b) 对，在我们希望考虑所有可能的组合的相似度时，比较有用
    （5） sample () 对RDD采样
     */


    println("$$$$$$$$$$$$$$行动操作￥￥￥￥￥￥￥￥￥￥￥￥￥￥")
    //行动操作，最常见的行动操作reduce，它介绍一个函数，这个函数要操作两个RDD的元素，返回一个同类型的新元素
    //val sum = rdd.reduce((x,y) => x+y)
    //fold 和reduce()一样，但是需要提供初始值  rdd.fold(0)((x, y) => x + y)
    val sum = distData.reduce((x,y) => x+y)
    println(sum)
    //求平均数
    val rdd = List(1,2,3,4,5,6,7,8,9)
    val agg = rdd.par.aggregate((0,0))(
      (acc,number) =>(acc._1+number,acc._2+1),
      (par1,par2) =>(par1._1+par2._1,par1._2+par2._2)
    )
    println(agg)

    //把数据返回驱动器城区中最简单，最常见的操作是collect(),他会将整个RDD的内存返回，
    //collect（）通常在单元测试的值使用，因为此时RDD的整个内容不会很大，可以在内存中使用，使用collect()使得RDD的值与预期结果
    //之间的对比变得很容易collect() 要求所有数据都必须能一同放入单台机器的内存中
//take(n) 返回 RDD 中的 n 个元素，并且尝试只访问尽量少的分区，因此该操作会得到一个不均衡的集合。需要注意的是，这些操作返回元素的顺序与你预期的可能不一样。
//如果为数据定义了顺序，就可以使用 top() 从 RDD 中获取前几个元素。 top() 会使用数据的默认顺序，但我们也可以提供自己的比较函数，来提取前几个元素。
//takeSample  对数据进行采样

    val cishu = distData.countByValue()
    println(cishu)











  }

}
