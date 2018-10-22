package main

import (
  "fmt"
  "os"
  "bufio"
  "log"
  "regexp"
)

func getDict() []string {
    file, err := os.Open("./dico.txt")
    if err != nil {
      log.Fatal(err)
    }
    defer file.Close()
    scanner := bufio.NewScanner(file)
    result := []string{}
    for scanner.Scan() {
        line := scanner.Text()
        result = append(result, line)
    }
    return result
}

func search(code string, dict []string) []string {
  d := map[string]string{
    "0": "(c[ieéèê]|[szç])",
    "1": "[td]",
    "2": "(n|gn)",
    "3": "m",
    "4": "r",
    "5": "l",
    "6": "([sc]h|g[eéèêiî]|j)",
    "7": "[gckqx]",
    "8": "(ph|[fvw])",
    "9": "[bp]"}
  _=d
  _=code

  var res []string

  x := "^[haàâeéèêëiîïoôöuùûyi-]*"
  for c:=0; c<len(code); c++{
    x += d[string(code[c])] + "[haàâeéèêëiîïoôöuùûyi-]*"
  }
  x += "$"
  re := regexp.MustCompile(x)

  for _, value := range dict {
    if re.MatchString(value){
      res = append(res, value)
    }
  }

  return res
}

func main(){
  dict := getDict()

  for i:=1; i<len(os.Args); i++{
    fmt.Println(" #" + os.Args[i]+" : ", search(os.Args[i], dict))
    fmt.Println("--------------")
  }

}
