/**
  * Created by zhangheng on 2017/8/31.
  */
object scaTestFunction {
  def main(args: Array[String]): Unit =
  {
    println("return value :"+ addInt(5,7));

    for (i<- 1 to 10)
      {
        println(i + " 的阶乘为：" + factorial(i))
      }
     val t = add(3,4);
    println(t)
  }
  //定义函数
  def addInt(a:Int,b : Int):Int =
  {
    var sum :Int = 0;
    sum = a+b;
      return sum ;
  }
  //递归函数
  def factorial(n: BigInt) : BigInt =
  {
    if (n <= 1) {
      return 1;
    }
    else {
      return n * factorial(n - 1);
    }




  }
  //这样都行
  def add(x:Int,y:Int) = x+y


}
