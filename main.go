package main

import (
        "log"
        "io"
        "net/http"
        "strconv"
)
var (
temp = ""
counter = 0
)

func Push(w http.ResponseWriter, req *http.Request) {
        temp = req.FormValue("temp")
        if temp != "" {
         counter = counter + 1
         }
}

func Get(w http.ResponseWriter, req *http.Request) { 
        io.WriteString(w, strconv.Itoa(counter))
}

func Reset(w http.ResponseWriter, req *http.Request) { 
        counter = 0
}

func main() {
        http.HandleFunc("/push", Push)
        http.HandleFunc("/get", Get)
        http.HandleFunc("/reset", Reset)
        err := http.ListenAndServe(":9100", nil)
        if err != nil {
                log.Fatal("ListenAndServe: ", err)
        }
}
