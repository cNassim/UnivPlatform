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
        { name: "Université de Toronto", country: "Canada", program: "Ingénierie", date: "01/04/2024" },
        { name: "Université de Sydney", country: "Australie", program: "Biotechnologie", date: "05/04/2024" },
        { name: "Université de Tokyo", country: "Japon", program: "Sciences de l'Informatique", date: "10/04/2024" }
    ];

    // Statut de l'étudiant
    const status = {
        currentStep: "Préparation des documents pour le visa",
        lastUpdate: "20/05/2024",
        nextStep: "Prendre rendez-vous pour le visa",
        additionalNotes: "Contacter l'université de Sydney pour confirmer la bourse"
    };

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
                             <td>${university.date}</td>`;
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
});
