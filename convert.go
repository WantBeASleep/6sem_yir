package main

import (
	"fmt"
	"log"
	"os/exec"
	"path/filepath"
	// "strconv"
)

// convertPDFToImages принимает путь к PDF файлу, выходной директории
// и префикс для имен выходных файлов.
func convertPDFToImages(pdfPath, outputDir, outputPrefix string) error {
	// Создание команды для pdftoppm
	cmd := exec.Command("pdftoppm", "-jpeg", pdfPath, filepath.Join(outputDir, outputPrefix))

	// Выполнение команды
	err := cmd.Run()
	if err != nil {
		return fmt.Errorf("ошибка при конвертации PDF в изображения: %v", err)
	}
	return nil
}

func main() {
	// Параметры конвертации
	pdfPath := "book.pdf"     // Путь к вашему PDF файлу
	outputDir := "output_images2" // Директория для сохранения изображений
	outputPrefix := "page_"      // Префикс для имен файлов изображений

	// Конвертация PDF в изображения
	err := convertPDFToImages(pdfPath, outputDir, outputPrefix)
	if err != nil {
		log.Fatalf("Ошибка: %v", err)
	}

	// Печать сообщения об успешной конвертации
	fmt.Println("PDF успешно конвертирован в изображения.")
}
