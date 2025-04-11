// Fonction pour obtenir un cookie par son nom
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

// Vérifier si l'utilisateur est authentifié et rediriger si non
function checkAuthentication() {
  const token = getCookie('token');
  if (!token) {
      window.location.href = 'index.html';  // Rediriger l'utilisateur non authentifié vers la page d'accueil
  }
  return token;
}

// Récupérer l'ID du lieu depuis l'URL
function getPlaceIdFromURL() {
  const urlParams = new URLSearchParams(window.location.search);
  return urlParams.get('id');
}

// Soumettre un avis
async function submitReview(token, placeId, reviewText, reviewRating) {
  try {
      const response = await fetch(`https://your-api-url/places/${placeId}/reviews`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${token}`
          },
          body: JSON.stringify({
              comment: reviewText,
              rating: reviewRating
          })
      });

      const responseData = await response.json();
      
      // Afficher un message de succès ou d'erreur
      if (response.ok) {
          document.getElementById('message').textContent = 'Review submitted successfully!';
          document.getElementById('review-form').reset();  // Réinitialiser le formulaire
      } else {
          document.getElementById('error-message').textContent = `Error: ${responseData.message || 'Something went wrong'}`;
      }
  } catch (error) {
      console.error('Error submitting review:', error);
      document.getElementById('error-message').textContent = 'Failed to submit review due to an error.';
  }
}

// Gérer la soumission du formulaire d'avis
document.addEventListener('DOMContentLoaded', () => {
  const reviewForm = document.getElementById('review-form');
  const token = checkAuthentication();  // Vérifier l'authentification
  const placeId = getPlaceIdFromURL();  // Extraire l'ID du lieu

  if (reviewForm) {
      reviewForm.addEventListener('submit', async (event) => {
          event.preventDefault();  // Empêcher l'envoi par défaut du formulaire
          
          const reviewText = document.getElementById('review-text').value;  // Récupérer le texte de l'avis
          const reviewRating = document.getElementById('review-rating').value;  // Récupérer la note

          // Soumettre l'avis à l'API
          await submitReview(token, placeId, reviewText, reviewRating);
      });
  }
});