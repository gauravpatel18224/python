#include <stdio.h>

void inputMatrix(int rows, int cols, int matrix[rows][cols]) {
    printf("Enter elements:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("Element [%d][%d]: ", i + 1, j + 1);
            scanf("%d", &matrix[i][j]);
        }
    }
}

void displayMatrix(int rows, int cols, int matrix[rows][cols]) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

void multiplyMatrices(int rows1, int cols1, int matrix1[rows1][cols1], int rows2, int cols2, int matrix2[rows2][cols2], int result[rows1][cols2]) {
    for (int i = 0; i < rows1; i++) {
        for (int j = 0; j < cols2; j++) {
            result[i][j] = 0;
            for (int k = 0; k < cols1; k++) {
                result[i][j] += matrix1[i][k] * matrix2[k][j];
            }
        }
    }
}

int main() {
    int rows1, cols1, rows2, cols2;

    printf("Matrix Multiplication\n");
    
    printf("--Matrix 1--\n");
    printf("Enter number of rows: ");
    scanf("%d", &rows1);
    printf("Enter number of columns: ");
    scanf("%d", &cols1);

    int matrix1[rows1][cols1];
    inputMatrix(rows1, cols1, matrix1);

    printf("--Matrix 2--\n");
    printf("Enter number of rows: ");
    scanf("%d", &rows2);
    printf("Enter number of columns: ");
    scanf("%d", &cols2);

    if (cols1 != rows2) {
        printf("Error: Number of columns of Matrix 1 must equal number of rows of Matrix 2.\n");
        return 1;
    }

    int matrix2[rows2][cols2];
    inputMatrix(rows2, cols2, matrix2);

    printf("\nMatrix 1:\n");
    displayMatrix(rows1, cols1, matrix1);
    printf("\nMatrix 2:\n");
    displayMatrix(rows2, cols2, matrix2);

    int result[rows1][cols2];
    multiplyMatrices(rows1, cols1, matrix1, rows2, cols2, matrix2, result);

    printf("\nResult: [Multiplication Matrix]\n");
    displayMatrix(rows1, cols2, result);

    return 0;
}
