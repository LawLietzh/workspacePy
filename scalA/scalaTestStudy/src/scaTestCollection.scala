/**
  * Created by zhangheng on 2017/9/1.
  */
object scaTestCollection {
  def main(args:Array[String]):Unit={

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
    /*
    ++ ++[B](that: GenTraversableOnce[B]): List[B] 从列表的尾部添加另外一个列表
    ++: ++:[B >: A, That](that: collection.Traversable[B])(implicit bf: CanBuildFrom[List[A], B, That]): That 在列表的头部添加一个列表
    +: +:(elem: A): List[A] 在列表的头部添加一个元素
    :+ :+(elem: A): List[A] 在列表的尾部添加一个元素
    :: ::(x: A): List[A] 在列表的头部添加一个元素
    ::: :::(prefix: List[A]): List[A] 在列表的头部添加另外一个列表
    :\ :[B](z: B)(op: (A, B) ⇒ B): B 与foldRight等价
     */
    val left = List(1,2,3)
    val right = List(4,5,6)
    println("//一下操作等价")
    //一下操作等价
    //列个列表相加
    println(left ++ right)
    //列个列表相加
    println(left ++: right)
    //把后面的列表 加到前面列表的前面
    println(right.++:(left))
    //把后面的列表 加到前面列表的前面
    println(right.:::(left))

    //一下操作也等价  可以看成 单个字符的时候，用单个加号
    println("一下操作也等价")
    println(0 +:left)//List(0,1,2,3)
    println(left.+:(0))

    println(left :+ 4)//List(1,2,3,4)
    println(left.:+(4)  )

    println(0 :: left) //List(0,1,2,3)
    println(left.::(0))

    /*
    这里给大家一个提示，任何以冒号结果的操作符，都是右绑定的，即 0 :: List(1,2,3) = List(1,2,3).::(0) = List(0,1,2,3) 从这里可以看出操作::其实是右边List的操作符，而非左边Int类型的操作符
     */
    println("**************map*************")
    // map  定义一个变换，把该变换应用到列表的每一个元素中，元列表不变，返回一个新的列表数据
    val nums = List(1,2,3)
    val square = (x:Int) => x*x
    val squareNum1 = nums.map(num => num*num)
    println(squareNum1)
    val squareNum2 = nums.map(math.pow(_,2))
    //传入一个匿名函数，返回 原列表中每一个元素 经过 该函数的结果
    val squareNum3 = nums.map(square)

    //保存文本数据的某几列
    var text = List("Homeway,25,Male","XSDYM,23,Female")
    val userList = text.map(_.split(",")(0))
    println(userList)

    text = List("A,B,C","D,E,F")
    //把列表中的元素，安装“，”分开，组成一个列表，这样每个元素都变成了一个列表
    val textMapped = text.map(_.split(",").toList)//List(List(A, B, C), List(D, E, F))
    println(textMapped)
    //就是把几个列表合成一个列表
    val textFlattened = textMapped.flatten// List("A","B","C","D","E","F")
    println(textFlattened)
    val textFlatMapped = text.flatMap(_.split(",").toList) // List("A","B","C","D","E","F")
    println(textFlatMapped)
    // reduce   列表求和

    val sum1 = nums.reduce((a,b) => a+b)   //6
    val sum2 = nums.reduce(_+_)            //6
    val sum3 = nums.sum                 //6




































  }

}
