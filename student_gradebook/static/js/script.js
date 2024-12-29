// Confirm deletion
function confirmDeletion(message) {
    return confirm(message);
  }
  
  // Delete student
  document.querySelectorAll('.delete-student').forEach(button => {
    button.addEventListener('click', event => {
      const studentId = event.target.dataset.studentId;
      const confirmed = confirmDeletion('Delete student?');
      if (confirmed) {
        window.location.href = `/delete_student/${studentId}`;
      }
    });
  });
  
  // Delete assignment
  document.querySelectorAll('.delete-assignment').forEach(button => {
    button.addEventListener('click', event => {
      const assignmentId = event.target.dataset.assignmentId;
      const confirmed = confirmDeletion('Delete assignment?');
      if (confirmed) {
        window.location.href = `/delete_assignment/${assignmentId}`;
      }
    });
  });
  
  // Delete grade
  document.querySelectorAll('.delete-grade').forEach(button => {
    button.addEventListener('click', event => {
      const gradeId = event.target.dataset.gradeId;
      const confirmed = confirmDeletion('Delete grade?');
      if (confirmed) {
        window.location.href = `/delete_grade/${gradeId}`;
      }
    });
  });
  
  // Toggle navbar on mobile
  document.querySelector('.navbar-toggler').addEventListener('click', () => {
    document.querySelector('.collapse').classList.toggle('show');
  });