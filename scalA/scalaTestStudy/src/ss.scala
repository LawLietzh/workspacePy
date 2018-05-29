/**
  * Created by zhangheng on 2017/8/30.
  */
import  scala.util.control._
object ss {
  def main(args: Array[String]) {
    // 输出 Hello World
    // 这是一个单行注释
    /*
    多行注释
     */
    println("Hello, world!")

    //声明变量
    var myVar : String  = "Foo"
     myVar  = "Too"
    println(myVar)
    //声明 常量
    val myVal:String = "doo"
    println(myVal)
    //测试 break 语句
    //创建break对象
    val loop = new Breaks;
    //在breakable中循环
    loop.breakable{
      var a = 10;
      while(a>0)
        {
          if (a == 3)
            {
              println(a)
              loop.break()
            }
          a -= 1
        }
      println("我在哪")
    }
    println("我出来了")


    //嵌套 循环
    var a = 0 ;
    var b = 0;
    val numList1 = List(1,2,3,4,5);
    val numList2 = List(11,12,13);

    val outer = new Breaks;
    val inner = new Breaks;

    outer.breakable{
      for(a <- numList1)
        {
          println("value of a :"+ a);
          inner.breakable
          {
            for( b <- numList2)
              {
                println("value of b ："+b);
                if(b == 12)
                  {
                    inner.break;
                  }
              }
          }






        }
    }
    println("*****************")

    //for 循环
    var aa = 0 ;
    for(aa <- 1 to 10)
    {
      println("value of a :"+ aa)
    }

    a = 0;
    b = 0;
    println("_____________________")
    for(a<- 1 to 3 ; b<- 1 to 3)
      {
        println("value of a :"+a);
        println("value of b :"+b );
      }

    println("&&&&&&&&&&&&")
    a = 0;
    val numlist = List(1,2,3,4,5,6,7,8);
    for(a <- numlist if a != 3;if a<=7)
      {
        println("value of a :"+ a);
      }
    println("yyyyyyyyyyyyyyyyyyyyyyy")
    //yield 关键字的使用
    var retVal = for{
      a <- numlist if a!=3 ;if a<=5
    }yield a ;
    //输出a
    for(a <- retVal)
      {
        println("value of a :"+ a);
      }

  }

}
