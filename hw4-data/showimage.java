import java.awt.AlphaComposite;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.image.BufferedImage;
import java.io.PrintWriter;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
 import java.io.BufferedReader;
 import java.io.FileReader;


public class showimage {
    public static void main(String [] args){
	if (args.length < 3){
	    System.out.println("Usage: Kmeans <original-image> <datafile> <output-image>");
	    return;
	}
	try{
	    BufferedImage originalImage = ImageIO.read(new File(args[0]));
	    //int k=Integer.parseInt(args[1]);
		//kmeans_helper(originalImage,args[1]);
	    BufferedImage kmeansJpg = kmeans_helper(originalImage,args[1]);
	    ImageIO.write(kmeansJpg, "jpg", new File(args[2])); 
	    
	}catch(IOException e){
	    System.out.println(e.getMessage());
	}	
    }
    
    private static BufferedImage kmeans_helper(BufferedImage originalImage, String cfile){
	int w=originalImage.getWidth();
	int h=originalImage.getHeight();
	BufferedImage kmeansImage = new BufferedImage(w,h,originalImage.getType());
	Graphics2D g = kmeansImage.createGraphics();
	g.drawImage(originalImage, 0, 0, w,h , null);
	BufferedReader br = null;
	try {
		int count=0;
		String sCurrentLine;
		int[] rgbarr=new int[w*h];
		br = new BufferedReader(new FileReader(cfile));
		//int count=0;
		while ((sCurrentLine = br.readLine()) != null) {
			String[] tokens = sCurrentLine.split(",");
			if(tokens.length>0) {
				int blue = Integer.parseInt(tokens[0]);
				int green = Integer.parseInt(tokens[1]);
				int red = Integer.parseInt(tokens[2]);
				int rgb = red;
				rgb = (rgb << 8) + green;
				rgb = (rgb << 8) + blue;
				rgbarr[count++] = rgb;
				//kmeansImage.setRGB(i,j,rgb);
			}
		}
		count=0;
		for(int i=0;i<w;i++){
			for(int j=0;j<h;j++){
			kmeansImage.setRGB(i,j,rgbarr[count++]);
			}
		}

	} catch (IOException e) {
		e.printStackTrace();
	} finally {
		try {
			if (br != null)br.close();
		} catch (IOException ex) {
			ex.printStackTrace();
		}
	}
	return kmeansImage;
	/*
	// Call kmeans algorithm: update the rgb values
	kmeans(rgb,k);

	// Write the new rgb values to the image
	count=0;
	for(int i=0;i<w;i++){
	    for(int j=0;j<h;j++){
		kmeansImage.setRGB(i,j,rgb[count++]);
	    }
	}
	return kmeansImage;*/
    }

    // Your k-means code goes here
    // Update the array rgb by assigning each entry in the rgb array to its cluster center
    private static void kmeans(int[] rgb, int k){
    }

}
