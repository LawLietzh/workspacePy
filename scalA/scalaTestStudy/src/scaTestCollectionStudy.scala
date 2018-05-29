/**
  * Created by zhangheng on 2017/9/1.
  * 练习scala集合 的使用  list  set
  */
object scaTestCollectionStudy {
  def main(args: Array[String]): Unit = {
    //字符串列表
    val site:List[String] = List("Runoob", "Google", "Baidu")
    //整型列表，
    val nums: List[Int] = List(1, 2, 3, 4)
    // 空列表
    val empty:List[Nothing] = List()
    //二维列表
    val dim : List[List[Int]] = List(List(1,0,0),List(0,1,0),List(0,0,1))
    //构造列表的两个基本单位是 Nil 和 ::
    //Nil可以表示为一个空列表
    println(dim)
    var sitee = "Runoob" ::("Google" :: ("Baidu"::Nil))//List(Runoob, Google, Baidu)

    println(sitee)
    sitee = "Runoob" ::"Google" :: "Baidu"::Nil  //和上一个  输出结果一样List(Runoob, Google, Baidu)
    println(sitee)
    /*
    列表的基本操作
    （1） head 返回列表的第一个元素
          tail 返回一个列表，包含出第一个元素之外的其他元素
          isEmpty 在列表为空时，返回true

     (2) 列表的链接
         ::: 正常顺序链接
         l1.:::(l2)  把l2加到l1 前面
         l1.concat(l2) 正常链接

      （3）我们可以使用 List.fill() 方法来创建一个指定重复数量的元素列表：

     */

    val ss = List.fill(3)("Run")//就是Run被重复三次
    // 通过给定的函数创建 5 个元素
    val squares = List.tabulate(6)(n => n * n)
    println( "一维 : " + squares  )

    // 创建二维列表
    val mul = List.tabulate( 4,5 )( _ * _ )//"????
    println( "多维 : " + mul  )

    // List.reverse   将列表顺序翻转

    println("ssssssssssssssssssssssssssssssssssssss")
    // Set 集合  ，没有重复的对象集合
    val set = Set(1,2,3)
    val swt2 = set.+(4)

    println(swt2)

    //可变set
    /*
    虽然可变Set和不可变Set都有添加或删除元素的操作，
    但是有一个非常大的差别。对不可变Set进行操作，会产生一个新的set，
    原来的set并没有改变，这与List一样。 而对可变Set进行操作，
    改变的是该Set本身，与ListBuffer类似。
     */
    import scala.collection.mutable.Set // 可以在任何地方引入 可变集合
    val mutableSet = Set(1,2,3)
    mutableSet.add(4)
    mutableSet.remove(1)
    println(mutableSet)
    val site1 = Set("Runoob", "Google", "Baidu")
    val site2 = Set("Faceboook", "Taobao")
    //set元素链接，没有顺序
    // ++ 作为运算符使用
    var ii = site1 ++ site2
    println( "site1 ++ site2 : " + ii )

    //  ++ 作为方法使用
    ii = site1.++(site2)
    println( "site1.++(site2) : " + ii )
    //可以使用 Set.& 方法或 Set.intersect 方法来查看两个集合的交集元素。实例如下：
    val num1 = Set(5,6,9,20,30,45)
    val num2 = Set(50,60,9,20,35,55)
    println( "num1.&(num2) : " + num1.&(num2) )
    println( "num1.intersect(num2) : " + num1.intersect(num2) )









  }

}
