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

fun main() {
    val lang: String = "Kotlin"
    /*val takeInput = readLine()!!.toString()
    println("Your input is: " + takeInput)*/
    println("Hello " + lang + " user! " + '(' + year + ')')
}

// Only run file lister if -d dirname has been passed as argument, passing only -d will result in an error
if (args.contains("-d")) filelister()

println("") // For new line
main()

