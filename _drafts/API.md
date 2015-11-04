---
title: "APIs"
author: "hjuinj"
date: "26 October 2015"
---

I recently gotten interested into APIs(application programming interfaces, not active pharmaceutical ingradients, which I am also interested in :D). This mainly stems from the idea of my second chrome plugin, which will involve interacting with youtube API. 
As I am ploughing through my code for this plugin I felt my methodology is not very systematic and I often run into problems which takes a while to look up online.  
So I decided to take a step back and spend some time on generic API usages.

This will espcially come in handy as I explore further usage of various other types of API services, such as my wanting to explore the chemical world using the CHEMBL (database) API (Though this will probably be mainly done in R rather than in JS).

So here is my study notes, which is based on [codeacademy's interactive courses](https://www.codecademy.com/courses/javascript-beginner-en-EID4t/0/1?curriculum_id=50ecb8d45f787a6332000042) on APIs

####RESTful Design
stands for Representational State Transfer
can be thought as a set of rules that the service provider and the service receiver have established to ensure secure, accurate, efficient interactions
I quote from codeacademy:

> 0. Separate the client from the server
> 1. Not hold state between requests (meaning that all the information necessary to respond to a request is available in each individual request; no data, or state, is held by the server from request to request)
> 2. Use HTTP and HTTP methods (GET, POST)

A request requires a method, a header and a optional body

A response takes form of a starting line with the status code, a header and a body which contains the data requested

Two primary data form are XML and Json. I personally like the Json format, which resembles that of Python dictionary data structure. XML seems a bit too pragmatic to me. JavaScript with Json( Java Script Object Notation) goes hand in hand. 

```javascript
var xhr = new XMLHttpRequest();
xhr.open("GET", "https://www.codecademy.com/", false);
xhr.send();

console.log(xhr.status);
console.log(xhr.statusText);
```

XML
```javascript
var xhr = new XMLHttpRequest();
xhr.open("GET", "https://www.codecademy.com/files/samples/javascript_learn_apis.xml", false);

xhr.setRequestHeader('Content-Type', 'text/xml');
xhr.send();

xmlDocument = xhr.responseXML;
console.log(xmlDocument.childNodes['0'].textContent);
```

jason
```javascript
var demo = '{"pets": { "name": "Jeffrey", "species": "Giraffe"}}';

var json = JSON.parse(demo);
console.log(json);
```


###Interacting with Youtube API
for querying youtube videos, which is also what I plan to aquire in my plugin/extension, one only needs to submit for an API key from [googld developer console](https://console.developers.google.com/project/boxwood-magnet-111023/apiui/credential)
requires an registration of a API key and OAuth2 authentication 




