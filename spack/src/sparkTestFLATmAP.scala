/**
  * Created by zhangheng on 2017/9/6.
  * 练习 faltMap 和map的区别
  * 而flatMap与map唯一不一样的地方就是传入的函数在处理完后返回值必须是List，
  * 其实这也不难理解，既然是flatMap，那除了map以外必然还有flat的操作，
  * 所以需要返回值是List才能执行flat这一步。
  */
object sparkTestFLATmAP {
  def main(args: Array[String]): Unit = {
    def flatMap1(): Unit = {
      val li = List(1,2,3)
      val res = li.flatMap(x => x match {
        case 3 => List('a','b')
        case _ => List(x*2)
      })
      println(res)
    }

    def map1(): Unit = {
      val li = List(1,2,3)
      val res = li.map(x => x match {
        case 3 => List('a','b')
        case _ => x*2
      })
      println(res)
    }

    def main(args: Array[String]): Unit = {
      flatMap1()
      map1()
    }
  }

}
