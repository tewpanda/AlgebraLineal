def generate_report(people, influencers, adj_matrix, laplacian, eigenvalues, eigenvectors):
    report = []
    report.append("INFORME DE INFLUENCERS EN LA RED SOCIAL\n")
    report.append(f"Personas analizadas: {', '.join(people)}\n")
    report.append(f"Influencers identificados: {', '.join(influencers)}\n")
    report.append("\nMatriz de Adyacencia:\n" + str(adj_matrix))
    report.append("\nMatriz Laplaciana:\n" + str(laplacian))
    report.append("\nValores propios de la Laplaciana:\n" + str(eigenvalues))
    report.append("\nVectores propios de la Laplaciana (columnas):\n" + str(eigenvectors))
    return '\n'.join(report)
