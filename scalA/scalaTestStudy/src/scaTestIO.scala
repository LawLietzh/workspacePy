/**
  * Created by zhangheng on 2017/9/2.
  * 练习 文件读写
  */
import  java.io._
object scaTestIO {
  def main(args: Array[String]): Unit = {
    //写文件
    val  writer  = new PrintWriter(new File("test.txt"),"UTF-8")
    writer.write("wo shi  cai niao ")
    writer.close()

    //有时候我们需要接收用户在屏幕输入的指令来处理程序。实例如下：
    println("请输入菜鸟教程官网 :")
    //val  line = StdIn.readLine()
    import scala.io.Source
    val source1 = Source.stdin
    println(source1)
    //读文件
    Source.fromFile("test.txt").foreach{
      print
    }
     println()
    val file = Source.fromFile("test.txt","UTF-8")
    /*
    可以把行列表存到数组中
    val = file.getLines.toArray
    也可以把整个文件 都城一个字符串
    val = file.getLines.mkString
     */
    for(line <- file.getLines)
      {
        println(line)
      }
    val iter = Source.fromFile("test.txt","UTF-8").buffered //遍历字符
    println("***************************")
    println(iter)
    while(iter.hasNext)
      {
        println(iter.head)
        iter.next()
      }

    file.close()
    //网络资源读取
    val webFile=Source.fromURL("http://spark.apache.org")
    //webFile.foreach(print)
    webFile.close()

    println("%6d  %10.2f".format(123456555,123456.334455))



  }

}
