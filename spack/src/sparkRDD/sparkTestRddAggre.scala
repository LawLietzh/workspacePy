package sparkRDD

/**
  * Created by zhangheng on 2017/9/7.
  * 求平均数   aggregate函数 执行过程
  */
object sparkTestRddAggre {
  def main(args: Array[String]): Unit = {
    val rdd = List(1,2,3,4,5,6,7,8,9)
    val agg = rdd.par.aggregate((0,0))(
      (acc,number) =>(acc._1+number,acc._2+1),
      (par1,par2) =>(par1._1+par2._1,par1._2+par2._2)
    )

    /*
    解释：(0,0) 是初始值，后面会用到
(acc,number) =>(acc._1+number,acc._2+1),中number 代表了rdd（1,2,3,4,5,6,7,8,9）
acc._1 和acc._2 的初始值就是（0,0）
在执行过程中，acc._1 和acc._2
1.   0+1,  0+1
2.  1+2,  1+1
3.  3+3,  2+1
4.  6+4,  3+1
5.  10+5,  4+1
6.  15+6,  5+1
7.  21+7,  6+1
8.  28+8,  7+1
9.  36+9,  8+1
从这个过程我们可以看出，acc._1 存的是rdd中数据相加，acc._2 在记录相加的次数，也就是list中的个数
结果即是(45,9)
这里演示的是单线程计算过程，实际Spark执行中是分布式计算，可能会把List分成多个分区，
假如3个，p1(1,2,3,4)，p2(5,6,7,8)，p3(9)，经过计算各分区的的结果（10,4），（26,4），（9,1），这样，
执行(par1,par2) => (par1._1 + par2._1, par1._2 + par2._2)就是
（10+26+9,4+4+1）即（45,9）.
再求平均值就简单了。







     */
    println(agg)


  }

}
