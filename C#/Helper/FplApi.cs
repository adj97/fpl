using RestSharp;
using Newtonsoft.Json;

namespace FplAnalysis.Helper
{
    class FplApi
    {
        public static RestRequest GetRequest()
        {
            RestRequest request = new RestRequest(Method.GET);
            return request;
        }

        public static dynamic ExecuteRequest(RestRequest request, string apiEndpoint)
        {
            // Full API uri
            string apiUri = MakeApiUri(apiEndpoint);

            // New client from input api endpoint
            RestClient client = new RestClient(apiUri);

            // Execute response, string output
            string responseContentJsonString = client.Execute(request).Content;

            // Use dynamic object from response to construct the ApiResponse
            return JsonConvert.DeserializeObject(responseContentJsonString);
        }

        private static string MakeApiUri(string apiEndpoint)
        {
            string apiBaseUri = UriString.baseApiUri;
            return apiBaseUri + apiEndpoint;
        }
    }
}
