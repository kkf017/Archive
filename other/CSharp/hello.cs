// mcs -out:hello.exe hello.cs
// mono hello.exe

using System;
using static Project.Player;

namespace Project {
    class MainClass {

        public static int func(int a, int b){
            return a * b;
        }
        
        public static void Main (string[] args) {
            Console.WriteLine ("Enter a number:");

	        int num = Convert.ToInt32(Console.ReadLine());
	        for(int i = 0; i<10; i++){
		        int x = func(num, i) ;
		        Console.WriteLine(x); 
		    }
                Console.ReadKey ();
            

            var play = new Player();
            play.name = "Play1";
            play.setValue(10);
            Console.WriteLine(play.getValue());
        }
    }
}
