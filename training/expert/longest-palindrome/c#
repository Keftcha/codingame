using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{
    static List<string> GetLongestPalindromes( string src )
    {
        List<string> palindromes;
        int i = 0;
        do
        {
            palindromes = GetLongestPalindromes( src, src.Length - i );
            i++;
        } while( palindromes.Count == 0 );
        return palindromes;
    }

    static List<string> GetLongestPalindromes( string src, int length )
    {
        List<string> palindromes = new List<string>();

        for( int i = 0; i < src.Length + 1 - length; i++ )
        {
            if( IsPalindrome( src, length, i ) )
            {
                palindromes.Add( src.Substring( i, length ) );
            }
        }

        return palindromes;
    }

    static bool IsPalindrome( string src, int length, int start )
    {
        for( int i = 0; i < length / 2; i++ )
        {
            if( src[ start + i ] != src[ start + length - i - 1 ] ) return false;
        }

        return true;
    }

    static void Main( string[] args )
    {
        string s = Console.ReadLine();
        List<string> longestPalindromes = GetLongestPalindromes( s );
        foreach( string p in longestPalindromes )
        {
            Console.WriteLine( p );
        }
    }
}
