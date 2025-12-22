package helpers

import (
	"encoding/json"
	"errors"
	"log"
	"net/http"
	"strings"

	"github.com/user-dashboard/models"
)

func parseJSONBody(r *http.Request, target interface{}) error {
	if r.Header.Get("Content-Type") != "application/json" {
		return errors.New("invalid content type")
	}

	decoder := json.NewDecoder(r.Body)
	decoder.DisallowUnknownFields()
	err := decoder.Decode(target)
	if err != nil {
		return err
	}

	return nil
}

func parseQueryString(r *http.Request, target interface{}) error {
	query := r.URL.Query()
	for key, value := range query {
		switch target := target.(type) {
		case *models.User:
			switch key {
			case "name":
				target.Name = strings.Join(value, "")
			case "email":
				target.Email = strings.Join(value, "")
			}
		}
	}

	return nil
}

func handleAPIError(w http.ResponseWriter, err error) {
	log.Println(err)
	http.Error(w, err.Error(), http.StatusInternalServerError)
}

func authenticateRequest(r *http.Request) (*models.User, error) {
	token := r.Header.Get("Authorization")
	if token == "" {
		return nil, errors.New("unauthorized")
	}

	// Assuming you have a function to verify the token
	user, err := verifyToken(token)
	if err != nil {
		return nil, err
	}

	return user, nil
}

func verifyToken(token string) (*models.User, error) {
	// Implement your token verification logic here
	// For demonstration purposes, assume the token is valid
	return &models.User{Name: "John Doe", Email: "john@example.com"}, nil
}