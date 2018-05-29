/**
  * Created by zhangheng on 2017/9/4.
  */
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf
import org.apache.spark.broadcast.Broadcast
import org.apache.spark.ml.feature.{OneHotEncoder, StringIndexer}
import org.apache.spark.ml.feature.{IndexToString, StringIndexer}
import org.apache.spark.mllib
import org.apache.spark.mllib.linalg.{Vector, Vectors}
import org.apache.spark.sql.hive.HiveContext
import org.apache.spark.sql.Row
import org.apache.spark.sql.types.{StructType,StructField,StringType}
import org.apache.spark.mllib.linalg.{Matrices, Matrix}
import org.apache.spark.mllib.linalg.distributed.RowMatrix
import org.apache.spark.mllib.linalg.distributed.IndexedRowMatrix
import org.apache.spark.mllib.linalg.SingularValueDecomposition
import org.apache.spark.rdd.RDD
import org.apache.spark.mllib.linalg.distributed.{CoordinateMatrix, MatrixEntry}
import org.apache.spark.mllib.linalg.{DenseMatrix}
import org.apache.spark.mllib.recommendation.ALS
import org.apache.spark.mllib.recommendation.MatrixFactorizationModel
import org.apache.spark.mllib.recommendation.Rating
object dd {

  def main(args: Array[String]): Unit = {
    val conf= new SparkConf().setAppName("wordcount")
    val sc=new SparkContext(conf)
    val line=sc.textFile("E://数据资料//spark//test.txt", 1)
    val word=line.flatMap(_.split(" "))
    val pairs=word.map(word => (word,1))
    val wordCounts=pairs.reduceByKey(_+_).map(x=>(x._2,x._1)).sortByKey(false, 1)
    val words=wordCounts.map(x=>x._2+":"+x._1+" ").foreach(println)
  }

}
