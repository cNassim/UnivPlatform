document.addEventListener('DOMContentLoaded', function() {
    // Données de l'étudiant
    const student = {
        name: "Marie Dupont",
        dob: "15/03/2002",
        id: "123456",
        email: "marie.dupont@example.com",
        phone: "+33 6 12 34 56 78"
    };

    // Universités ciblées
    const universities = [
        { name: "Université de Toronto", country: "Canada", program: "Ingénierie", date: "01/04/2024", status: "En attente", notes: "-" },
        { name: "Université de Sydney", country: "Australie", program: "Biotechnologie", date: "05/04/2024", status: "Acceptée", notes: "Bourse offerte" },
        { name: "Université de Tokyo", country: "Japon", program: "Sciences de l'Informatique", date: "10/04/2024", status: "Rejetée", notes: "-" }
    ];

    // Statut de l'étudiant
    const status = {
        currentStep: "Préparation des documents pour le visa",
        lastUpdate: "20/05/2024",
        nextStep: "Prendre rendez-vous pour le visa",
        additionalNotes: "Contacter l'université de Sydney pour confirmer la bourse"
    };

    // Historique des mises à jour
    const updates = [
        { date: "20/05/2024", update: "Acceptation de l'université de Sydney", comments: "Offre de bourse reçue" },
        { date: "15/05/2024", update: "Rejet de l'université de Tokyo", comments: "-" },
        { date: "01/05/2024", update: "Candidature à l'université de Toronto soumise", comments: "En attente de réponse" }
    ];

    // Actions à entreprendre
    const actions = [
        "Passeport (ok)",
        "Relevés de notes (ok)",
        "Lettre de recommandation (en cours)",
        "Certificat de langue (en cours)",
        "Soumettre la candidature à [Nom Université 1]",
        "Soumettre la candidature à [Nom Université 2]",
        "Vérifier le statut de l'université de Toronto le 01/06/2024",
        "Prendre rendez-vous pour le visa australien",
        "Rechercher un logement à Sydney"
    ];

    // Remplir les informations de l'étudiant
    if (document.getElementById('student-name')) {
        document.getElementById('student-name').textContent = student.name;
        document.getElementById('dob').textContent = student.dob;
        document.getElementById('student-id').textContent = student.id;
        document.getElementById('email').textContent = student.email;
        document.getElementById('phone').textContent = student.phone;
    }

    // Remplir les universités ciblées
    if (document.getElementById('universities-body')) {
        const universitiesBody = document.getElementById('universities-body');
        universities.forEach(university => {
            let row = document.createElement('tr');
            row.innerHTML = `<td>${university.name}</td>
                             <td>${university.country}</td>
                             <td>${university.program}</td>
                             <td>${university.date}</td>
                             <td>${university.status}</td>
                             <td>${university.notes}</td>`;
            universitiesBody.appendChild(row);
        });
    }

    // Remplir le statut de l'étudiant
    if (document.getElementById('current-step')) {
        document.getElementById('current-step').textContent = status.currentStep;
        document.getElementById('last-update').textContent = status.lastUpdate;
        document.getElementById('next-step').textContent = status.nextStep;
        document.getElementById('additional-notes').textContent = status.additionalNotes;
    }

    // Remplir l'historique des mises à jour
    if (document.getElementById('updates-body')) {
        const updatesBody = document.getElementById('updates-body');
        updates.forEach(update => {
            let row = document.createElement('tr');
            row.innerHTML = `<td>${update.date}</td>
                             <td>${update.update}</td>
                             <td>${update.comments}</td>`;
            updatesBody.appendChild(row);
        });
    }

    // Remplir les actions à entreprendre
    if (document.getElementById('actions-list')) {
        const actionsList = document.getElementById('actions-list');
        actions.forEach(action => {
            let item = document.createElement('li');
            item.textContent = action;
            actionsList.appendChild(item);
        });
    }
});
