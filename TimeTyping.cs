public static int TimeTyping(){

	// returns the the number of seconds user spent typing input

  	int startM = DateTime.Now.Minute;
        int startS = DateTime.Now.Second;
        Console.ReadLine();
        int endM = DateTime.Now.Minute;
        int endS = DateTime.Now.Second;
        int deltaM = Math.Abs(endM - startM);
        int deltaS;
        if(deltaM == 0){
        	deltaS = Math.Abs(startS - endS);
       	}else{
		deltaS = Math.Abs(deltaM * 60 - startS) + endS; 
             }

	return deltaS;	

}