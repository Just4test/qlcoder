// http://www.qlcoder.com/train/handsomerank
// http://www.qlcoder.com/task/7647
package main

import (
    "fmt"
	"strings"
    "net/http"
    "io/ioutil"
    "crypto/md5"
    "strconv"
    "time"
)

func main() {
    // fmt.Println(getPrefix(`just4test`, `y4jvl2NXFdWcCALS2ZyX6WmkB67QWfvey5syrJqC`))
    // fmt.Printf("%x", md5.Sum([]byte(`20160422just4test1`)))
    // // fmt.Println(`20160422just4test1` + string(1123123))
    // fmt.Println(calc(`just4test`, `y4jvl2NXFdWcCALS2ZyX6WmkB67QWfvey5syrJqC`))
    for{
        calc(`just4test`, `1`)
    }
}

func submit(user,token,checkcode string) string{
    url := fmt.Sprintf(`http://www.qlcoder.com/train/handsomerank?_token=%s&user=%s&checkcode=%s`,
    token, user, checkcode)
    response, _ := http.Get(url)
    defer response.Body.Close()
    body, _ := ioutil.ReadAll(response.Body)
    // fmt.Println(string(body))
    return string(body)
}

func getPrefix(user, token string)string{
    for{
        body := submit(user, token, ``)
        if 0 == strings.Index(body, `验证码错误`) {
            temp := strings.Split(body, `"`)
            return temp[1]
        }
    }
}

func calc(user, token string) string {
    prefix := getPrefix(user, token)
    num := 0
    var result string
    startTime := time.Now()
    for {
        result = strconv.Itoa(num)
        temp := fmt.Sprintf(`%x`, md5.Sum([]byte(prefix + result)))
        // fmt.Println(`MD5(%s) = %s`, result, temp, num)
        if 0 == strings.Index(temp, `000000`) {
            fmt.Println(`MD5(%s) = %s \n用时%d毫秒`, result, temp, time.Since(startTime))
            submit(user, token, result)
            return result
        }
        num ++
        
    }
}