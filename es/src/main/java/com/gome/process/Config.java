package com.gome.process;

import java.io.IOException;
import java.util.Properties;

public class Config {
	//读取配置文件的类
	static Properties properties;
	static{
		properties = new Properties();
		try {
			//加载配置文件，方便下文中 getProperty 使用
			properties.load(Config.class.getClassLoader().getResourceAsStream("config.properties"));
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public static String clustername = properties.getProperty("es.cluster.name");
	public static String esip = properties.getProperty("es.cluster.ip");
	public static int esport = Integer.parseInt(properties.getProperty("es.cluster.port"));
	public static String esdatabase = properties.getProperty("es.database");
	public static String estable = properties.getProperty("es.table");


}
