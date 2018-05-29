/**
  * Created by zhangheng on 2017/8/31.
  */
object scaTestString {
  def main(args: Array[String]): Unit = {
    val gree = "Hello ,World";
    val gre :String = "Hello ,World";
    println(gree)
    println(gre)
    /*
    String 对象是不可变的，如果你需要创建一个 可以修改的字符串，可以使用String Builder类
     */
    val buf = new StringBuilder;
    // 'a'  改成"a"  就不可以了
    //也可以写成 buf +='a'
    buf.+('a');
    buf ++= "bcdef";
    println("buf is :"+buf.toString());
    //字符串长度
    var len = buf.length();
    println(len)
    //字符串连接
    val str1 = "hello ";
    //也可以直接用 +
    val str2 =str1.concat(" ssss");
    println(str2)
    //创建格式化字符串
    var floatVar = 12.345;
    var intVar = 2000;
    var stringVar = "菜鸟教程";
    println("浮点型变量为 %f, 整型变量为 %d, 字符串为 %s", floatVar, intVar, stringVar);
    /*
      Scala 中的字符串的方法还有：
      charAt()
     */

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

    //使用range()方法来 生成一个区间范围内的数组
    //range 不识别，新版本的是Range
    var myList3 = Range(10,20,2)
    var myList4 = Range(10,20)
    for( a  <- myList3)
    {
      println(a)
    }
    for( a  <- myList4)
    {
      println(a)
    }


    println("**********************")
    //集合  list  set  map
    //list

    val mainlist = List(3,2,1)
    println(mainlist)
    //在列表开通加入 4
    val with4 = 4::mainlist
    println(with4)
    val with42 = 42::mainlist
    println(with42)
    // 返回 除第一个元素 后面的元素
    val shorer = with4.tail
    println(shorer)
    val days = List("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

    // Make a list element-by-element
    val when = "AM" :: "PM" :: List()
    println(when)

    // Pattern match
    days match {
      case firstDay :: otherDays =>
        println("The first day of the week is: " + firstDay)
      case List() =>
        println("There don't seem to be any week days.")
    }










  }

}
