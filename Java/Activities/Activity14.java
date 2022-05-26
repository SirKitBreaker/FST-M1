package activities;

import org.apache.commons.io.FileUtils;
import java.io.File;
import java.io.IOException;

public class Activity14 {

    public static void main(String[] args) throws IOException {

        String path = "C:\\Users\\0005Z4744\\testFile.txt";
        File file = new File(path);
        //check if file is created or not
        boolean fStatus = file.createNewFile();
        if (fStatus) {
            System.out.println("File is created");
        } else {
            System.out.println("File is not created");
        }
        File newFile = FileUtils.getFile(path);
        FileUtils.write(newFile, "Hello This is my first file", "UTF-8");
        System.out.println("Data in file: " + FileUtils.readFileToString(newFile, "UTF8"));

        //Create directory
        File destDir = new File("C:\\Users\\0005Z4744\\IdeaProjects\\FST39-Java\\src\\main\\resources");
        //Copy file to directory
        FileUtils.copyFileToDirectory(newFile, destDir);

        //Get file from new directory
        File destFile = FileUtils.getFile(destDir, "testFile.txt");
        //Read data from file
        System.out.println("Data in new file: " + FileUtils.readFileToString(destFile, "UTF8"));
    }
}
