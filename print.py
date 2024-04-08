# Python 脚本用于创建文件并写入不同编程语言的 "Hello, World!" 代码

# 定义一个包含文件扩展名和对应的编程语言打印语句的字典
code_templates = {
    '.c': '#include <stdio.h>\n\nint main() {\n    printf("Hello, World!\\n");\n    return 0;\n}',
    '.cpp': '#include <iostream>\n\nint main() {\n    std::cout << "Hello, World!" << std::endl;\n    return 0;\n}',
    '.java': 'public class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n    }\n}',
    '.py': 'print("Hello, World!")',
    '.js': 'console.log("Hello, World!");',
    '.cs': 'using System;\n\nclass HelloWorld {\n    static void Main(string[] args) {\n        Console.WriteLine("Hello, World!");\n    }\n}',
    '.rb': 'puts "Hello, World!"',
    '.php': '<?php\necho "Hello, World!";\n?>',
    '.go': 'package main\n\nimport "fmt"\n\nfunc main() {\n    fmt.Println("Hello, World!");\n}',
    '.swift': 'import Foundation\n\nprint("Hello, World!")',
    '.rs': 'fn main() {\n    println!("Hello, World!");\n}',
    '.kt': 'fun main() {\n    println("Hello, World!")\n}',
    '.ts': 'console.log("Hello, World!");',
    '.scala': 'object HelloWorld {\n  def main(args: Array[String]): Unit = {\n    println("Hello, World!")\n  }\n}',
    '.hs': 'main :: IO ()\nmain = putStrLn "Hello, World!"',
    '.pl': 'use strict; use warnings;\nprint "Hello, World!\\n";',
    '.lua': 'print("Hello, World!")',
    '.ex': 'IO.puts "Hello, World!"',
    '.clj': '(ns hello-world)\n(defn -main []\n  (println "Hello, World!"))\n',
    '.fs': 'open System\nprintfn "Hello, World!"',
    '.dart': 'import \'dart:io\';\n\nvoid main() {\n  print("Hello, World!");\n}',
    '.elm': 'import System\n\nmain = System.print "Hello, World!"',
    '.bash': 'echo "Hello, World!"',
    '.ps1': 'Write-Host "Hello, World!"',
    '.vb': 'Imports System\n\nModule HelloWorld\n    Sub Main()\n        Console.WriteLine("Hello, World!")\n    End Sub\nEnd Module',
    '.jl': 'println("Hello, World!")',
    '.cr': 'puts "Hello, World!"',
    '.nim': 'echo "Hello, World!"'
}


for extension, code in code_templates.items():
    filename = f"hello_world{extension}"

    with open(filename, 'w') as file:
        file.write(code)
    print(f"File '{filename}' has been created with the corresponding 'Hello, World!' code snippet.")

print("All files have been created with corresponding 'Hello, World!' code snippets for each programming language.")
