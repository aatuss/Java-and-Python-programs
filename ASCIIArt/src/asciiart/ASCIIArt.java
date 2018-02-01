import java.io.*;
import java.util.Scanner;
 
class ASCIIArt {
    // ohjelman on tehnyt Aleksi Lahtinen, opiskelijanumero: 4424411
    
    //ohjelman toiminta on jaettu useampaan operaatioon, mutta päätoiminnallisuus tapahtuu
    //main metodissa
    //ohjelmassa on vaikoidut komennot, joita käyttäjä syöttää sekä myös "MERKIT" taulukko on vakio attribuutti
    //Komennot ajetaan main metodissa ja komennon perusteella ajetaan haluttu metodi.

    //Operaatiot:
    //kopioiTaulukko operaatio kopioi taulukon,
    //tulostaLuvut tulostaa kuvan lukuina
    //,lataa metodi lataa kuvan
    //,suodata metodissa tapahtuu suodatustoiminto
    //komennot myös syötetään omassa metodissaan
    //mediaani operaatiolla saadaan tarvittavat mediaanit taulukosta
    //tulosta määrät tulostaa eri merkkien määrät, tulostaluvut tulostaa kuvan "lukuina"
    //tulostaTaulukko metodi tulostaa taulukot merkkeinä
   
   private static final String PRINTA = "printa";
   private static final String PRINTI = "printi";
   private static final String INFO = "info";
   private static final String FILTER = "filter";
   private static final String RESET = "reset";
   private static final String QUIT = "quit";
   //Merkkitaulukko
   private static final char[] MERKIT = {
         '#',
         '@',
         '&',
         '$',
         '%',
         'x',
         '*',
         'o',
         '|',
         '!',
         ';',
         ':',
         '\'',
         ',',
         '.',
         ' '
      };
    
   //Kopioi taulukon
   public static char[][] kopioiTaulukko(char[][] taulukko) {
      char[][] palautus = new char[taulukko.length][taulukko[0].length];
      //Käydään taulukko läpi ja lisätään uuteen taulukkoon merkit
      if (taulukko != null) {
      for (int y = 0; y < taulukko.length; y++) {
         for (int x = 0; x < taulukko[y].length; x++) {
            palautus[y][x] = taulukko[y][x];
            }
         }
      }
      return palautus;
   }
   
   //Lataa kuvan
   public static char[][] lataa(String nimi) {
      try {
         //Ladataan nimen mukainen tiedosto
         Scanner tiedosto = new Scanner(new FileReader(nimi));
         tiedosto.useDelimiter("xxdelimiterxx");
         char[][] taulu = null;
         char[][] palautus = null;
         int i = 0;
         //Käydään tiedosto läpi
         while(tiedosto.hasNext()) {
            String rivi = tiedosto.nextLine();
            //Jos ensimmäinen rivi, lisätään suoraa palautettavaan taulukkoon
            if (i == 0) {
               palautus = new char[1][rivi.length()];
               palautus[0] = rivi.toCharArray();
            } else {
               //Muutoin kopioidaan vanha taulukko ja lisätään uusi rivi
               taulu = new char[palautus.length + 1][rivi.length()];
               for (int y = 0; y < palautus.length; y++) {
                  for (int x = 0; x < palautus[y].length; x++) {
                     taulu[y][x] = palautus[y][x];
                  }
               }
               taulu[taulu.length - 1] = rivi.toCharArray();
               palautus = taulu;
            }
            i++;
         }
         return palautus;
      } catch(Exception e) {
         e.printStackTrace();
         return null;
      }
   }
   
   //Tulostaa kuvan lukuina
   public static void tulostaLuvut(char[][] taulukko) {
     
      
      //Käydään kuva läpi
      if (taulukko != null){
      for (int y = 0; y < taulukko.length; y++) {
         for (int x = 0; x < taulukko[y].length; x++) {
            for (int i = 0; i < MERKIT.length; i++) {
               //Verrataan läpikäytävää merkkiä taulukkoon ja tulostetaan indeksi
               if (taulukko[y][x] == MERKIT[i]) {
                  if (String.valueOf(i).length() < 2)
                     System.out.print(" " + i);
                  else
                     System.out.print(i);
               }
            }
            if (x != taulukko[y].length - 1)
               System.out.print(" ");
         }
         System.out.println();
        }
      }
   }
   
   //Tulostaa yksittäisten merkkien määrät ja koon
   public static void tulostaMaarat(char[][] taulukko) {
      if (taulukko != null) {
      //Luodaan taulukko merkkien määrille
          int[] maarat = new int[MERKIT.length];
      
      //Käydään kuva läpi
          for (int y = 0; y < taulukko.length; y++) {
             for (int x = 0; x < taulukko[y].length; x++) {
                for (int i = 0; i < MERKIT.length; i++) {
                //Verrataan läpikäytävää merkkiä taulukkoon ja lisätään määrää
                   if (taulukko[y][x] == MERKIT[i]) {
                      maarat[i]++;
                    }
                }
            }
       }
      //Tulostetaan koko ja merkkien määrät
      System.out.println(taulukko.length + " x " + taulukko[0].length);
      for (int i = 0; i < MERKIT.length; i++)
         System.out.println(MERKIT[i] + " " + maarat[i]);
       }
      
   }
   
   //Tulostaa taulukon merkkeinä
   public static void tulostaTaulukko(char[][] taulukko) {
      if (taulukko != null) {
         //Käydään taulukko läpi ja tulostetaan merkki
         for (int y = 0; y < taulukko.length; y++) {
            for (int x = 0; x < taulukko[0].length; x++)
               System.out.print(taulukko[y][x]);
            System.out.println();
         }
      }
   }
   
   //Suodattaa taulukon
   public static char[][] suodata(char[][] taulukko, int koko) {
      
      
      //Otetaan reunuksen koko
      int reunus = (koko / 2);
      char[] suodin = new char[koko * koko];
      int i = 0;
      //Luodaan taulukko palautusta varten
      char[][] palautus = kopioiTaulukko(taulukko);
      if (taulukko != null){
      //Käydään kuva läpi lukuunottamatta reunusta
          for (int y = reunus; y < taulukko.length - reunus; y++) {
             for (int x = reunus; x < taulukko[y].length - reunus; x++) {
                i = 0;
            //Käydään läpikäytävän kohdan ympäröivä osuus koon perusteella
            //ja lisätään arvot taulukkoon
                for (int fy = y - reunus; fy <= y + reunus; fy++) {
                   for (int fx = x - reunus; fx <= x + reunus; fx++) {
                      suodin[i] = taulukko[fy][fx];
                      i++;           
                    }
                }
            //Otetaan suodatinosiotaulukosta mediaani ja lisätään se 
            //palautettavaan taulukkoon
            palautus[y][x] = mediaani(suodin);
           }
       }
      
      }
      return palautus;
      
   }
   
   //Palauttaa taulukosta mediaanin
   public static char mediaani(char[] taulukko) {
      
      
      //Muutetaan merkit kokonaisluvuiksi
      int[] jarjestetty = new int[taulukko.length];
      if (taulukko != null){
          for (int i = 0; i < taulukko.length; i++) {
             for (int u = 0; u < MERKIT.length; u++) {
                if (taulukko[i] == MERKIT[u])
                   jarjestetty[i] = u;
            
                }
           }
           int sijainti = 0;
           int vaihto;
      //Käydään luvut läpi
           while (sijainti < taulukko.length) {
         //Jos ensimmäinen luku tai aijempi luku on pienempi, lisätään käytävää indeksiä
                if (sijainti == 0 || jarjestetty[sijainti] >= jarjestetty[sijainti - 1]) {
                   sijainti++;
               } else {
            //Jos luku on isompi, vaihdetaan paikkoja aijemman kanssa ja vähennetään käytävää indeksiä
                vaihto = jarjestetty[sijainti];
                jarjestetty[sijainti] = jarjestetty[sijainti - 1];
                jarjestetty[sijainti - 1] = vaihto;
                sijainti--;
           }
        }
      
      
      }
      return MERKIT[jarjestetty[jarjestetty.length / 2]];
   }
   //Komentojen syöte
   public static void komento(String nimi) {
      String[] syote = { "", "" };
      //Ladataan kuva 
      char[][] taulukko = lataa(nimi);
      //Kysytään komentoa kunnes lopetetaan
      while (syote[0] != QUIT) {
         System.out.println("printa/printi/info/filter [n]/reset/quit?");
         syote[0] = In.readString();
         syote = syote[0].split(" ");
         //Tarkastetaan syöte
         switch (syote[0]) {
            case PRINTA:
               tulostaTaulukko(taulukko);
            break;
            case PRINTI:
               tulostaLuvut(taulukko);
            break;
            case INFO:
               tulostaMaarat(taulukko);
            break;
            case FILTER:
               //Jos ei ole parametrejä, toteutetaan suodatus oletusarvolla
               if (syote.length == 2)
                  taulukko = suodata(taulukko, Integer.parseInt(syote[1]));
               else
                  taulukko = suodata(taulukko, 3);
            break;
            case RESET:
               taulukko = lataa(nimi);
            break;
            case QUIT:
               return;
         }
      }
   }
   
   public static void main(String[] args) {
      System.out.println("-------------------");
      System.out.println("| A S C I I A r t |");
      System.out.println("-------------------");
      if (args != null) {
         File tiedosto = new File(args[0]);
         if (tiedosto.exists() && !tiedosto.isDirectory() && args.length == 1)
            komento(args[0]);
         else
            System.out.println("Invalid command-line argument!");
      }
      System.out.println("Bye, see you soon.");
   }
}