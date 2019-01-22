public class Kata {
	public static String getIssuer(String cardNumber) {
		int cardNumLength = cardNumber.length();
		
		switch(cardNumLength) {
		case 13 :
		case 16 :
			if(cardNumber.substring(0, 1).equals("4"))
				return "VISA";
			if(cardNumber.substring(0, 2).equals("51") || cardNumber.substring(0, 2).equals("52") || cardNumber.substring(0, 2).equals("53") || cardNumber.substring(0, 2).equals("54") || cardNumber.substring(0, 2).equals("55") )
				return "Mastercard";
			if(cardNumber.substring(0, 4).equals("6011"))
				return "Discover";
			break;
		
		case 15 :
			if(cardNumber.substring(0, 2).equals("34") || cardNumber.substring(0, 2).equals("37"))
				return "AMEX";
			break;
		}
		return "Unknown";
	}
}