package com.juvenxu.mvnbook.helloworld;
import com.mongodb.MongoClient;
import com.mongodb.client.MongoDatabase;

import com.mongodb.MongoClient;
import com.mongodb.MongoClientOptions;
import com.mongodb.MongoCredential;
import com.mongodb.ServerAddress;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import com.mongodb.BasicDBObject;
import com.mongodb.BulkWriteOperation;
import com.mongodb.BulkWriteResult;
import com.mongodb.Cursor;
import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.DBCursor;
import com.mongodb.DBObject;
import com.mongodb.MongoClient;
import com.mongodb.ParallelScanOptions;
import com.mongodb.ServerAddress;
import java.util.List;
import java.util.Set;
import static java.util.concurrent.TimeUnit.SECONDS;

/**
 * Created by zhangheng on 2017/11/8.
 */
public class MongoTest {
    public  static void  main(String[] args)
    {

        //MongoClient mongoClient = new MongoClient();
       // MongoClient mongoClient = new MongoClient( "localhost" );
             //连接到mongodb 服务
        MongoClient mongoClient = new MongoClient( "localhost" , 27017 );
       // MongoDatabase mongoDatabase = mongoClient.getDatabase("local");
        // or, to connect to a replica set, with auto-discovery of the primary, supply a seed list of members
       /* MongoClient mongoClient = new MongoClient(Arrays.asList(new ServerAddress("localhost", 27017),
                new ServerAddress("localhost", 27018),
                new ServerAddress("localhost", 27019)));*/

        DB db = mongoClient.getDB( "local" );

        DBCollection coll = db.getCollection("col");
        System.out.println(coll);
        BasicDBObject doc = new BasicDBObject("name", "MongoDB")
                .append("type", "database")
                .append("count", 1)
                .append("info", new BasicDBObject("x", 203).append("y", 102));
        coll.insert(doc);
        DBObject myDoc = coll.findOne();
        System.out.println(myDoc);

        DBCursor cursor = coll.find();
        try {
            while(cursor.hasNext()) {
                System.out.println(cursor.next());
            }
        } finally {
            cursor.close();
        }

    }


}
