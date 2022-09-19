#!/usr/bin/env kscript
// Imports
import java.io.File

// Vars
var year: Int = 2022

// Functions
fun filelister() {
    // Get the passed in path, i.e. "-d some/path" or use the current path.
    val path = if (args.contains("-d")) args[1 + args.indexOf("-d")]
        else "."
    val folders = File(path).listFiles { file -> file.isDirectory() }
    folders?.forEach { folder -> println(folder) }
}

fun calcSumDigit() {
    val digit = if (args.contains("-csd")) args[1 + args.indexOf("-csd")].toInt()
        else 0
    var num = digit
    var sum = 0
    while (num != 0) {
        sum = sum + num % 10
        num = num / 10
    }
    println("The sum of " + digit.toString() + " is " + sum.toString())
}

fun main() {
    val lang: String = "Kotlin"
    /*val takeInput = readLine()!!.toString()
    println("Your input is: " + takeInput)*/
    println("Hello " + lang + " user! " + '(' + year + ')')
}

// Only run file lister if -d dirname has been passed as argument, passing only -d will result in an error
if (args.contains("-d")) filelister()
// Only run sum calculator of digit if -csd int has been passed as argument, passing only -csd will result in an error
if (args.contains("-csd")) calcSumDigit()

println("") // For new line
main()

