import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import org.json.JSONObject;

public class CurrencyConverter {

    private static final String API_KEY = "TU_API_KEY_AQUI";
    private static final String API_URL = "https://v6.exchangerate-api.com/v6/" + API_KEY + "/latest/";

    public static double getExchangeRate(String fromCurrency, String toCurrency) throws IOException, InterruptedException {
        String urlStr = API_URL + fromCurrency;
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(urlStr))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        if (response.statusCode() != 200) {
            throw new RuntimeException("Failed to get response from API");
        }

        JSONObject json = new JSONObject(response.body());
        return json.getJSONObject("conversion_rates").getDouble(toCurrency);
    }

    public static double convertCurrency(String fromCurrency, String toCurrency, double amount) throws IOException, InterruptedException {
        double rate = getExchangeRate(fromCurrency, toCurrency);
        return amount * rate;
    }

    public static void main(String[] args) {
        try {
            String fromCurrency = "USD";
            String toCurrency = "EUR";
            double amount = 100;
            double result = convertCurrency(fromCurrency, toCurrency, amount);
            System.out.println(amount + " " + fromCurrency + " = " + result + " " + toCurrency);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
