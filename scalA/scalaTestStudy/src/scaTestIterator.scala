/**
  * Created by zhangheng on 2017/9/2.
  */
object scaTestIterator {
  def main(args: Array[String]): Unit = {
    //迭代器 迭代器 it 的两个基本操作是 next 和 hasNext。
    val it = Iterator("Baidu", "Google", "Runoob", "Taobao")

    while(it.hasNext)
      {
        println(it.next())
      }
    //可以使用 it.min 和 it.max 方法从迭代器中查找最大与最小元素，实例如下
    //你可以使用 it.size 或 it.length 方法来查看迭代器中的元素个数。实例如下：




  }

}
