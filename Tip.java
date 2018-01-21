import java.util.Scanner;
import java.util.stream.DoubleStream;
public class Tip {
	public static void main(String[]args) {
		/*user input function*/
		Scanner xy= new Scanner(System.in);
		int ppl, num=4;
		double[] items =new double[num];
		System.out.print("Enter each item separated with a space: ");
		for(int i= 0; i<items.length; i++) {
			items[i] = xy.nextDouble(); // store user input into array
		}
		double total = DoubleStream.of(items).sum(); //sums up every items in array
		System.out.print("Total(not including tax+tips) is "+total+" dollars with "+num+" items.");
		
		/* Tax function*/
		double tax, taxRate;
		System.out.print("\nEnter amount of tax charged: ");
		tax = xy.nextDouble();
		
		taxRate = (tax/total)*100;
		taxRate =Math.round(taxRate*100.0)/100.0;
		
		System.out.print("Tax Rate: "+taxRate+"%");
		//System.out.print("\n");
		
		
		/* Tip function*/
		double tip, tipRate;
		
		System.out.print("\nEnter number of people and tip percentage: ");
		ppl = xy.nextInt();
		tipRate = xy.nextDouble()/100;
		tip = Math.round(((tipRate*total)/ppl)*100.0)/100.0;
		
		System.out.print("Each person pays "+tip+" dollars for tips");
		
		
	}
}
