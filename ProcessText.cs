using System;
using System.Collections.Generic;
using System.Linq;

// some tools for text processing 

public class ProcessText
{
    private static string[][] syntax =
    {
        new string[] { "the", "an", "a" }, //0 articles
        new string[] { "most","that","this","these","what","every","all","any","few","my"}, //1 determiners
        new string[] { "on", "in", "to", "of", "at", "from", "for", "with","about","after","before","by"},//2 prepositions  
        new string[] {"if","for","and","nor","but","or","yet","so","which","as","then","when"},//3 conjuctions
        new string[] {"have","has","had"},//4 possesive verb
        new string[] {"be","that's","is","are","were","was","being","will","would","can","could","does","do"},//5 pos state
        new string[] {"not","isn't","aren't","weren't","wasn't","won't","wouldn't","can't","couldn't","doesn't","don't"},//6 neg state
    };

    // Remove punctuation 
    public static void StripPunct(string[] text, List<string> result)
    {
        for (int i = 0; i < text.Length; i++)
        {
            string word = text[i];
            result.Add(word.TrimEnd('.', ',', ';', ':', '!', '?', '/'));
        }
    }

    // Extract sentences from text and store them seperately, strip punctuation 
    public static void ExtractSentences(string[] textRaw, List<string[]> sentencesList)
    {
        List<string> tmp = new List<string>();

        // convert sentences into punctuation-less strings, put into tmp
        string str = "";
        for (int i = 0; i < textRaw.Length; i++)
        {
            str += textRaw[i].TrimEnd(',', '!', '?', ':', ';','/') + " ";
            for (int j = 0; j < textRaw[i].Length; j++)
            {
                // don't start new statement if the word is a common abbreviation 
                if (textRaw[i] != "mr." && textRaw[i] != "mrs." && textRaw[i] != "dr." && textRaw[i] != "dr." && textRaw[i] != "p.s." && textRaw[i] != "u.s." && textRaw[i] != "u.s.a")
                {
                    if (textRaw[i][j] == '.' || textRaw[i][j] == '?' || textRaw[i][j] == '!') 
                    {
                        str = str.TrimEnd(' '); 
                        tmp.Add(str.TrimEnd('.'));
                        str = "";
                        j++; // skip spaces in front of new sentences
                    }
                }
            }
        }
        // put each stripped sentence (string) from tmp into its own string[] 
        for (int s = 0; s < tmp.Count(); s++)
        {
            string[] stc = tmp[s].Split();
            sentencesList.Add(stc);
        }
    }



    // Remove articles, prepositions, and conjunctions after extracting sentences from text
    // put result into new list of sentences 
    public static void SimplifySentences(List<string[]> sentences, List<string[]> result)
    {
       
        for (int s = 0; s < sentences.Count(); s++)
        {
            string str = "";
            for (int w = 0; w < sentences[s].Length; w++) // go through each word in sentence
            {
                if (syntax[0].Contains(sentences[s][w])) // if word in wordtype list, skip index, add next word to string
                {
                    w++;
                    str += sentences[s][w] + " ";
                }
                else if (syntax[2].Contains(sentences[s][w])) 
                {
                    w++;
                    if (syntax[2].Contains(sentences[s][w]))  // nested 'if' in case wordtype appears twice
                    {                                         // e.g. "in of"      
                        w++;                                
                        str += sentences[s][w] + " ";
                    }
                    else
                    {
                        str += sentences[s][w] + " ";
                    }
                }
                else if (syntax[3].Contains(sentences[s][w]))
                {
                    w++;
                    if (syntax[3].Contains(sentences[s][w]))
                    {
                        w++;
                        str += sentences[s][w] + " ";
                    }
                    else
                    {
                        str += sentences[s][w] + " ";
                    }
                }else{
                        str += sentences[s][w] + " ";
                }
             }
                result.Add(str.Split());
            }

        }





 
    }
}




   




