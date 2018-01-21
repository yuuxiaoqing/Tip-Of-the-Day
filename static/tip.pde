import java.util.Scanner;
import java.util.stream.DoubleStream;
public class Tip2 {
	public static void main(String[]args) {
		/*user input function*/
		Scanner xy= new Scanner(System.in);
		int ppl, num=4;
		double[] items =new double[num];
		System.out.print("Enter each item separated with a space: ");
		for(int i= 0; i<items.length; i++) {
			items[i] = xy.nextDouble(); // store user input into array
		}
		double total = 0;
		for(int i=0; i<items.length; i++) {
			total +=items[i]; //sums up every items in array
		}
		System.out.print("Total(not including tax+tips) is "+total+" dollars with "+num+" items.");
		
		/* Tax function*/
		double tax, taxRate, taxPercent;
		System.out.print("\nEnter amount of tax charged: ");
		tax = xy.nextDouble();
		
		taxRate = (tax/total)*100;
		taxPercent =Math.round(taxRate*100.0)/100.0;
		
		System.out.print("Tax Rate: "+taxPercent+"%");
		System.out.print("\nEnter the items you're gonna pay for: ");
		double [] price = new double[2];
		for(int i=0; i<price.length; i++) {
			price[i]=xy.nextDouble();
		}
		double priceTotal = 0;
		for(int i =0; i<price.length; i++) {
			priceTotal += price[i];
		}
		
		tax = priceTotal*(taxRate/100);
		
		System.out.print("Tax amount for you: "+tax);
		
		/* Tip function*/
		double tip, tipRate;
		
		System.out.print("\nEnter tip percentage you want to pay: ");
		//ppl = xy.nextInt();
		tipRate = xy.nextDouble()/100;
		tip = Math.round((tipRate*priceTotal)*100.0)/100.0;
		
		System.out.print("You pay "+tip+" dollars for tips");
		
		/*Subtotal for each person*/
		
		double subTotal = Math.round((priceTotal+tax+tip)*100.0)/100.0;
		System.out.print("\nYou pay: "+subTotal);
		
		