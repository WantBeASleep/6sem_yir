package main

import (
	"fmt"
	"os"
	"path/filepath"

	"golang.org/x/text/encoding/charmap"
	"golang.org/x/text/transform"
)

func main() {
	// Путь к папке с HTML файлами
	inputDir := "/home/wantbeasleep/yirDetectKruk/bukvar"
	// Имя выходного файла
	outputFile := "res.html"

	// Открываем выходной файл для записи
	out, err := os.Create(outputFile)
	if err != nil {
		fmt.Printf("Ошибка при создании выходного файла: %v\n", err)
		return
	}
	defer out.Close()

	// Проходим по всем HTML файлам в заданной папке
	err = filepath.Walk(inputDir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		// Если это не файл, пропускаем его
		if !info.Mode().IsRegular() {
			return nil
		}
		// Читаем содержимое файла
		content, err := os.ReadFile(path)
		if err != nil {
			return fmt.Errorf("не удалось прочитать файл %s: %v", path, err)
		}

		// Создаем трансформер для преобразования из Windows-1251 в UTF-8
		decoder := charmap.Windows1251.NewDecoder()
		utf8Content, _, err := transform.String(decoder, string(content))
		if err != nil {
			return fmt.Errorf("не удалось преобразовать содержимое файла %s: %v", path, err)
		}

		// Пишем преобразованное содержимое в выходной файл
		if _, err := out.WriteString(utf8Content); err != nil {
			return fmt.Errorf("не удалось записать в выходной файл: %v", err)
		}

		fmt.Printf("Файл %s успешно обработан и добавлен\n", path)
		return nil
	})

	if err != nil {
		fmt.Printf("Ошибка при обработке файлов: %v\n", err)
	}

	fmt.Println("Все файлы успешно объединены и преобразованы!")
}
