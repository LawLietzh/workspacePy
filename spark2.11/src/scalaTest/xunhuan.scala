package scalaTest

/**
  * Created by zhangheng on 2017/10/30.
  * 练习 scala  循环
  */
object xunhuan {
  def main(args: Array[String]): Unit = {


    //to
    for (i <- 1 to 3){
      println(i)
    }
    //相当于
    val range = (1 to 3)
    range.foreach(println)
    // until  用until 的时候，是[）
    for(i<- 1 until 3)
      {
        println("i:",i)

      }

    // 多范围
    for(i <-1 to 3 ;j<- 1 to 3)
      {

      }
    //相当于
    for( i <-1 to 3 ){
           for(j <- 1 to 3)
            {

            }
    }

    //List
    val list = List(1,2,3)
    for(elem <- list){
      println(elem)
    }
    //条件
    val list2 = List(1,2,3,4,5,6)
    for(i <- list2 if i !=3;if i<5)
      {
        println(i)
      }
    //yield 返回for循环中符合条件的变量值 并组成被遍历的类型

    var retVal = for{i <- list2 if i!=3;if i<5} yield i
    for(i<- retVal)
      {
        println("i:"+i)
      }







  }

}
