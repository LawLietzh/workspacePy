/**
  * Created by zhangheng on 2017/9/1.
  */
object scaTestArray {

  def main(args:Array[String]): Unit =
    {
      var z = new Array[String](3)
      //var z:Array[String] = new Array[String](3)
      // var z = Array("Runoob", "Baidu", "Google")
      //赋值
      z(0) = "a"
      z(1) = "b"
      z(2) = "c"
      // 数组的遍历
      for( a  <- z)
      {
        println(a)
      }
      for(i <- 0 to (z.length -1))
      {
        println(z(i))
      }

      //scala 提供了 大量的集合操作
      val a = Array(1,2)
      val b = Array(3,4)
      //c 是 1，2,3,4
      val c = a ++ b
      // 区别在于，返回结果的类型 有b 决定
      //val c = a ++:b
      println(c.apply(0))
      //在数组开头加一个 0
      val d = 0 +: a
      println(d)
      //val d = 0 :+ a  找数组后面加一个0
      val e = List(1,2,3,4)
      //把 10 和 e 中数据，安装后面的运算符，
      val f = (10 /:e)(_+_)   // 1+2+3+4+10
      println(f)
      //将数组中的元素  逐个添加到b中
      val aa = List(1,2,3,4)
      val bb = new StringBuilder()
      //将a中元素加到bb中 然后付给 cc
       var  cc = aa.addString(bb)
      println(cc)
      println("*********")
      println(bb)

      println("*********")
      val bb1 = new StringBuilder()
      //添加aa中元素的中间，添加， 结果为 1,2,3,4
      val vv = aa.addString(bb1,",")
      println(vv)

















    }

}
