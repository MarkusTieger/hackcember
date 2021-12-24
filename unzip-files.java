package de.MarkusTieger;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.util.Random;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

public class App {

    private static int count = 0;

    public static void main(String[] args) throws IOException {

        File file = new File("challenge.zip");
        unzip(file, "temp.zip");

    }

    public static void unzip(File target, String tmp) throws IOException {

        count++;
        System.out.println(count);

        File temp = new File(tmp);

        if(temp.exists()) Files.delete(temp.toPath());

        FileInputStream in = new FileInputStream(target);
        ZipInputStream zis = new ZipInputStream(in);
        ZipEntry ze = zis.getNextEntry();
        if(ze == null) throw new IOException("NULL");
        if(ze.getName().toLowerCase().endsWith(".zip")) {
            if(!temp.exists()) temp.createNewFile();
            FileOutputStream o = new FileOutputStream(temp);
            int len;
            byte[] buffer = new byte[1024];
            while((len = zis.read(buffer)) > 0){
                o.write(buffer, 0, len);
                o.flush();
            }
            zis.closeEntry();
            zis.close();
            o.close();
            unzip(temp, temp.getName().equalsIgnoreCase("temp.zip") ? "tmp.zip" : "temp.zip");
        } else {
            if(!temp.exists()) temp.createNewFile();
            FileOutputStream o = new FileOutputStream(temp);
            int len;
            byte[] buffer = new byte[1024];
            while((len = zis.read(buffer)) > 0){
                o.write(buffer, 0, len);
                o.flush();
            }
            zis.closeEntry();
            o.close();
            temp.renameTo(new File("data" + new Random().nextInt()));

            while((ze = zis.getNextEntry()) != null){
                if(!temp.exists()) temp.createNewFile();
                o = new FileOutputStream(temp);
                while((len = zis.read(buffer)) > 0){
                    o.write(buffer, 0, len);
                    o.flush();
                }
                zis.closeEntry();
                o.close();
                temp.renameTo(new File("data" + new Random().nextInt()));
            }

            zis.close();
        }
    }

}