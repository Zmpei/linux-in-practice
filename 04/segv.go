package main

import "fmt"

func main() {
	// nilは必ずアクセスに失敗してページフォールトが発生する特殊なメモリアクセス
	var p *int = nil
	fmt.Println("不正メモリアクセス前")
	*p = 0
	fmt.Println("不正メモリアクセス後")
}
