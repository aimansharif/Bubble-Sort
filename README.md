# Programming-Practice
Programming Practice Problems

Batch File to start MongoDB process 

@echo off 
cd "C:\Program Files\MongoDB\Server\4.4\bin" 
start mongod.exe 
timeout 4 
start mongo.exe 
exit
